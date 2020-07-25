# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

 
# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
import random
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

# Forms
# from rasa_sdk.events import SlotSet, FollowupAction
# from rasa_sdk.forms import FormAction

# Connect to DigiCult API with All Institutions, no Details
base = "https://kultursphaere.sh/corsproxy.php?url=http://xtree-actor-api.digicult-verbund.de/getRepositoryList?portalURI=http://digicult.vocnet.org/portal/p0287&count=9999&lang=de"
r = requests.get(base)
data = r.json()
dataAccess = data['Actor']

def getInstitutionByName(institutionList,name):
        for institutionData in institutionList:
            if(institutionData['name'] == name):
                return institutionData

def filterInstitutionsByLocation(institutionList,location):
        filteredList = []
        for institutionData in institutionList:
            if(institutionData['place'] == location):
                filteredList.append(institutionData)
        return filteredList

def filterInstitutionsByCategory(institutionList,category):
        translatedCategory = translateCategoryKey(category)
        controlURI = f"http://digicult.vocnet.org/portal/{translatedCategory}"
        filteredList = []
        for institutionData in institutionList:
            classData = institutionData['classification']
            if (any(controlURI in classAccess.values() for classAccess in classData)):
                filteredList.append(institutionData)
        return filteredList

def filterInstitutionsByTag(institutionList,tag):
        translatedTag = translateTagKey(tag)
        filteredList = []
        for institutionData in institutionList:
            tagData = institutionData['icon']
            if (any(translatedTag in sl.values() for sl in tagData)):
                filteredList.append(institutionData)
        return filteredList

# Translations
categories = {
        "Draußen" : "p0264",
        "Film" : "p0294",
        "Wissen & Natur" : "p0295",
        "Musik" : "p0296",
        "Museum & Ausstellung" : "p0297",
        "Literatur" : "p0298",
        "Bühne" : "p0299",
}

tags = {
    "Kostenfrei" : "opt001",
    "Parkplatz" : "opt004",
    "Regelmäßige Führungen" : "opt006",
    "Angebot für Sehbehinderte" : "opt012",
    "Angebot für Hörbehinderte" : "opt013",
    "Angebot für geistig Behinderte" : "opt014",
    "Barrierefrei zugänglich" : "opt017",
    "Behindertenparkplatz" : "opt020",
    "Shop" : "opt021",
    "Gastronomie" : "opt022",
    "Behinderten-WC" : "opt024",
    "Familienfreundlich" : "opt033",
    "Angebot für Schulklassen" : "opt035",
    "Schietwetter" : "opt036",
    "Open Air" : "opt037",
    "MuseumsCard" : "opt039",
    "Angebot auf Englisch" : "optlang_en",
    "Angebot auf Dänisch" : "optlang_dk"
}

def translateCategoryKey(category):
    for c in categories.keys():
        if(c == category):
            return categories[c]

def translateTagKey(tag):
    for t in tags.keys():
        if(t == tag):
            return tags[t]

# Connect to DigiCult Detail API

def getInstitutionDetail(institutionID):
        actID = institutionID
        baseDetail = f"https://kultursphaere.sh/corsproxy.php?url=http://xtree-actor-api.digicult-verbund.de/getRepositoryItem?id={actID}&lang=de"
        rDetail = requests.get(baseDetail)
        dataDetail = rDetail.json()
        return dataDetail

def getInfoData(descriptionData, infoData):
        for info in descriptionData:
            if(info['id'] == infoData):
                descriptionNotes = info['noteValue'] 
                description = descriptionNotes[0]
                return description
        return ""

def getInstitutionDescription(institutionID):
        dataDetail = getInstitutionDetail(institutionID)
        descriptionData = dataDetail['Actor']['description']
        institutionDescription = getInfoData(descriptionData, "info029")
        return institutionDescription

def getInstitutionAddressAsString(institutionID):
        dataDetail = getInstitutionDetail(institutionID)
        addressData = dataDetail['Actor']['address']
        addressAccess = addressData[0]
        street = addressAccess['street']
        zipCode = addressAccess['zip']
        place = addressAccess['place']
        addressString = f"{street}, {zipCode} {place}"
        return addressString

def checkCategoryInInstitution(institutionID, category):
        translatedCategory = translateCategoryKey(category)
        controlURI = f"http://digicult.vocnet.org/portal/{translatedCategory}"
        dataDetail = getInstitutionDetail(institutionID)
        catData = dataDetail['Actor']['classification']
        if (any(controlURI in sl.values() for sl in catData)):
            return True
        else:
            return False

def checkTagInInstitution(institutionID, tag):
        dataDetail = getInstitutionDetail(institutionID)
        tagData = dataDetail['Actor']['icon']
        translatedTag = translateTagKey(tag)
        if (any(translatedTag in sl.values() for sl in tagData)):
            return True
        else:
            return False

class ActionGetInstitution(Action):

    def name(self) -> Text:
        return "action_get_institution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # get Data
        institutionList = dataAccess.copy()
        location = tracker.get_slot("location")
        category = tracker.get_slot("institution_category")
        tag = tracker.get_slot("institution_tag")
        
        print("Data:")
        print(location)
        print(category)
        print(tag)

        # Strings
        locationString = ""
        categoryString = ""
        tagString = ""

        if location:
            institutionList = filterInstitutionsByLocation(institutionList, location)
            locationString = f" in {location}"
        if category:
            institutionList = filterInstitutionsByCategory(institutionList, category)
            categoryString = f" in der Kategorie \"{category}\""
        if tag:
            institutionList = filterInstitutionsByTag(institutionList, tag)
            tagString = f" mit dem Angebot \"{tag}\""
        if institutionList:
            institution = getRandomInstitution(institutionList)
            name = institution['name']
            description = getInstitutionDescription(institution['id'])
            address = getInstitutionAddressAsString(institution['id'])
            dispatcher.utter_message(text=f"Hier ist mein Tipp" + locationString + categoryString + tagString + ":")
            dispatcher.utter_message(text=f"{name}")
            dispatcher.utter_message(text=f"{description}")
            dispatcher.utter_message(text=f"{address}")
            return [SlotSet("institution", institution)]
        else:
            dispatcher.utter_message(text=f"Ich konnte leider nichts" + locationString + categoryString + tagString + " finden.")
            dispatcher.utter_message(text=f"Vielleicht finde ich etwas, wenn du den Ort, die Kategorie oder das Angebot wechselst.")
            return ""

class ActionGetInstitutionByName(Action):

    def name(self) -> Text:
        return "action_get_institution_by_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # get Data
        institutionList = dataAccess.copy()
        name = tracker.get_slot("institution_name")
        
        print("Data:")
        print(name)

        if name:
            institution = getInstitutionByName(institutionList, name)
        if institution:
            description = getInstitutionDescription(institution['id'])
            address = getInstitutionAddressAsString(institution['id'])
            dispatcher.utter_message(text=f"Alles klar, hier sind ein paar Informationen zu der Institution {name}:")
            dispatcher.utter_message(text=f"{description}")
            dispatcher.utter_message(text=f"{address}")
            return [SlotSet("institution", institution)]
        else:
            dispatcher.utter_message(text=f"Ich konnte leider keine Institution mit dem Namen \"{name}\" finden :(.")
            dispatcher.utter_message(text=f"Du kannst im kulturfinder.sh nach der Institution suchen. Oder gebe eine andere Formulierung des Namens an, nach dem ich suchen soll.")
            return ""

# BunkerD = getInstitutionByName(dataAccess,"Bunker-D")
# print(getInstitutionAddressAsString(BunkerD['id']))

class ActionCheckInstitutionAttributes(Action):

    def name(self) -> Text:
        return "action_check_institution_attributes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # get Data
        institutionList = dataAccess.copy()
        name = tracker.get_slot("institution_name")
        # name = tracker.get_slot("institution_name")
        # location = tracker.get_slot("check_location")
        category = tracker.get_slot("institution_category")
        tag = tracker.get_slot("institution_tag")
        
        print("Data:")
        print(name)
        print(category)
        print(tag)

        # Strings
        # locationString = ""
        categoryString = ""
        tagString = ""

        if name:
            institution = getInstitutionByName(institutionList, name)
            if institution:
                if category:
                    if checkCategoryInInstitution(institution['id'], tag):
                        tagString = f"Ja, {name} ist in der Kategorie  \"{category}\"."
                    else:
                        tagString = f"Nein, {name} ist leider nicht in der Kategorie  \"{category}\"."
                if tag:
                    if checkTagInInstitution(institution['id'], tag):
                        tagString = f"Ja, das Angebot  \"{tag}\" ist vorhanden."
                    else:
                        tagString = f"Nein, das Angebot \"{tag}\" ist leider nicht vorhanden."
                
                dispatcher.utter_message(text=f"Ich habe mal im {name} nachgegeschaut:")
                dispatcher.utter_message(text=categoryString)
                dispatcher.utter_message(text=tagString)
                return [SlotSet("institution", institution)]
            else:
                dispatcher.utter_message(text=f"Ich konnte leider keine Institution mit dem Namen \"{name}\" finden :(.")
                dispatcher.utter_message(text=f"Du kannst im kulturfinder.sh nach der Institution suchen. Oder gebe eine andere Formulierung des Namens an, nach dem ich suchen soll.")
                return ""