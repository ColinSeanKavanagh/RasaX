## happy offer institution path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* inform_institution_location{"institution_location": "Kiel"}
  - utter_ask_institution_category

* inform_institution_category{"institution_category": "Musik & Ausstellung"}
  - utter_ask_institution_tag

* inform_institution_tag{"institution_tag": "Familienfreundlich"}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else

* deny
  - utter_happy
  - utter_goodbye

## happy name information path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp
* inform_offer{"offer":"Informationen"}
  - utter_ask_institution_name
* inform_institution_name{"institution_name":"Bunker-D"}
  - action_get_institution_by_name
  - utter_ask_feedback
* affirm
  - utter_happy
  - utter_anything_else
* deny
  - utter_happy
  - utter_goodbye

## happy check information path
* inform_offer{"institution_name":"Bunker-D", "institution_category": "Draußen", "institution_tag": "Parkplatz"}
  - action_check_institution_attributes
  - utter_ask_feedback
* affirm
  - utter_happy
  - utter_anything_else
* deny
  - utter_happy
  - utter_goodbye

## happy check tag path
* inform_offer{"institution_name":"Bunker-D", "institution_tag": "Parkplatz"}
  - action_check_institution_attributes
  - utter_ask_feedback
* affirm
  - utter_happy
  - utter_anything_else
* deny
  - utter_happy
  - utter_goodbye

## happy check category path
* inform_offer{"institution_name":"Bunker-D", "institution_category": "Familienfreundlich"}
  - action_check_institution_attributes
  - utter_ask_feedback
* affirm
  - utter_happy
  - utter_anything_else
* deny
  - utter_happy
  - utter_goodbye

## happy fast offer institution path
* inform_offer{"offer":"Tipp", "institution_category": "Museum & Ausstellung", "institution_tag": "Familienfreundlich"}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution with location path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* inform_institution_location{"offer": "Tipp","institution_location": "Kiel"}
  - utter_ask_institution_category

* deny
  - utter_ask_institution_tag
  - slot{"institution_category": ""}

* deny
  - slot{"institution_tag": ""}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution with location and category path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* inform_institution_location{"institution_location": "Kiel"}
  - utter_ask_institution_category

* inform_institution_category{"institution_category": "Bühne"}
  - utter_ask_institution_tag

* deny
  - slot{"institution_tag": ""}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution location and tag path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* inform_institution_location{"institution_location": "Kiel"}
  - utter_ask_institution_category

* deny
  - utter_ask_institution_tag
  - slot{"institution_category": ""}

* inform_institution_tag{"institution_tag": "Familienfreundlich"}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution with category path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* deny
  - utter_ask_institution_category
  - slot{"institution_location": ""}

* inform_institution_category{"institution_category": "Bühne"}
  - utter_ask_institution_tag

* deny
  - slot{"institution_tag": ""}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution category and tag path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* deny
  - utter_ask_institution_category
  - slot{"institution_location": ""}

* inform_institution_category{"institution_category": "Musik & Ausstellung"}
  - utter_ask_institution_tag

* inform_institution_tag{"institution_tag": "Familienfreundlich"}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## happy offer institution tag path
* greet
  - utter_greet
  - utter_introduction
  - utter_offer_tipp

* affirm OR inform_offer{"offer":"Tipp"}
  - utter_ask_institution_location

* deny
  - utter_ask_institution_category
  - slot{"institution_location": ""}

* deny
  - utter_ask_institution_tag
  - slot{"institution_category": ""}

* inform_institution_tag{"institution_tag": "Familienfreundlich"}
  - action_get_institution
  - utter_ask_feedback

* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp

* deny
  - utter_happy
  - utter_goodbye

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_ask_feedback
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - utter_cheer_up
  - utter_ask_feedback
* deny
  - utter_sorry
  - utter_ask_feedback
  - utter_offer_tipp
* deny
  - utter_sorry
  - utter_cheer_up
  - utter_ask_feedback

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## out of scope
* out_of_scope
  - utter_unsure
  - utter_offer_tipp

## out of scope II
* out_of_scope
  - utter_unsure
  - utter_offer_tipp
* deny
  - utter_sorry
  - utter_ask_feedback
* affirm
  - utter_offer_tipp

## interactive_story_1
* greet
    - utter_greet
    - utter_introduction
    - utter_offer_tipp
* affirm
    - utter_ask_institution_location
* inform_institution_location{"institution_location": "Kiel"}
    - slot{"institution_location": "Kiel"}
    - utter_ask_institution_category
* inform_institution_category{"institution_category": "Museum & Ausstellung"}
    - slot{"institution_category": "Museum & Ausstellung"}
    - utter_ask_institution_tag
* inform_institution_tag{"institution_tag": "Familienfreundlich"}
    - slot{"institution_tag": "Familienfreundlich"}
    - action_get_institution
    - utter_ask_feedback
* deny
    - utter_offer_tipp
* affirm
    - utter_ask_institution_location
* inform_institution_location{"institution_location": "Lübeck"}
    - slot{"institution_location": "Lübeck"}
    - utter_ask_institution_category
* inform_institution_category{"institution_category": "Literatur"}
    - slot{"institution_category": "Literatur"}
    - utter_ask_institution_tag
* inform_institution_tag{"institution_tag": "Familienfreundlich"}
    - slot{"institution_tag": "Familienfreundlich"}
    - action_get_institution
    - slot{"institution": {"id": "act001462", "name": "Buddenbrookhaus: Heinrich-und-Thomas-Mann-Zentrum", "nameAddition": "Buddenbrookhaus Lübeck", "place": "Lübeck", "street": "Mengstraße 4", "ISIL": "DE-MUS-441812", "pos": "10.6857702 53.8683189", "teaser": "Heinrich-und-Thomas-Mann-Zentrum", "icon": [{"type": "general", "id": "opt024"}, {"type": "general", "id": "opt034"}, {"type": "general", "id": "opt039"}, {"type": "general", "id": "opt003"}, {"type": "general", "id": "opt021"}, {"type": "general", "id": "opt033"}, {"type": "general", "id": "opt036"}, {"type": "general", "id": "opt018"}, {"type": "general", "id": "opt032"}, {"type": "general", "id": "opt035"}, {"type": "general", "id": "opt006"}], "classification": [{"type": "kulturtyp", "uri": "http://digicult.vocnet.org/portal/p0103"}, {"type": "tourismustyp", "uri": "http://digicult.vocnet.org/portal/p0297"}, {"type": "tourismustyp", "uri": "http://digicult.vocnet.org/portal/p0298"}], "resource": {"resourceRepresentation": {"type": "image_thumbnail", "link": "https://museumsbilder.digicult-verbund.de/thumbnail/m5dd52a5a08e54/Buddenbrookhaus%3A+Heinrich-und-Thomas-Mann-Zentrum/Buddenbrookhaus+Frontansicht"}}}}
    - utter_ask_feedback
* thanks
    - utter_happy
    - utter_anything_else
    - utter_offer_another_tipp
* affirm
    - utter_ask_reset
* affirm
    - slot{"institution_name":"","institution_location":"","institution_category":"","institution_tag":""}
    - utter_ask_institution_location
* inform_institution_location{"institution_location": "Heide"}
    - slot{"institution_location": "Heide"}
    - utter_ask_institution_category
* inform_institution_category{"institution_category": "Draußen"}
    - slot{"institution_category": "Draußen"}
    - utter_ask_institution_tag
* deny
    - action_get_institution
    - utter_ask_feedback
* affirm
  - utter_happy
  - utter_anything_else
  - utter_offer_another_tipp
* deny
  - utter_happy
  - utter_goodbye

## New Story

* inform_institution_tag{"institution_name":"Bunker-D","institution_tag":"Barrierefrei zugänglich"}
    - slot{"institution_name":"Bunker-D"}
    - slot{"institution_tag":"Barrierefrei zugänglich"}
    - action_check_institution_attributes
    - slot{"institution":{"id":"act0002152","name":"Bunker-D","place":"Kiel","street":"Schwentinestraße 11","pos":"10.179224 54.332743","teaser":"Freie Gedanken und Aktionen in festen Wänden.","icon":[{"type":"general","id":"opt002"},{"type":"general","id":"opt022"},{"type":"general","id":"opt004"},{"type":"general","id":"opt003"},{"type":"general","id":"opt036"}],"classification":[{"type":"kulturtyp","uri":"http://digicult.vocnet.org/portal/p0104"},{"type":"kulturtyp","uri":"http://digicult.vocnet.org/portal/p0102"},{"type":"tourismustyp","uri":"http://digicult.vocnet.org/portal/p0297"},{"type":"kulturtyp","uri":"http://digicult.vocnet.org/portal/p0270"},{"type":"tourismustyp","uri":"http://digicult.vocnet.org/portal/p0294"},{"type":"tourismustyp","uri":"http://digicult.vocnet.org/portal/p0296"}],"resource":{"resourceRepresentation":{"type":"image_thumbnail","link":"https://museumsbilder.digicult-verbund.de/thumbnail/m5b4cd21ea4c65/Bunker-D/Bunker-D"}}}}
    - utter_ask_feedback
* affirm
    - utter_happy
    - utter_anything_else
* affirm
    - utter_happy
    - utter_goodbye

## New Story

* greet
    - utter_greet
    - utter_introduction
    - utter_offer_tipp
* inform_offer{"offer":"Tipp"}
    - utter_ask_institution_location
* inform_institution_location{"institution_location":"Schleswig-Holstein"}
    - slot{"institution_location":"Schleswig-Holstein"}
    - utter_ask_institution_category
* deny
    - utter_ask_institution_tag
* deny
    - action_get_institution
    - slot{"institution":{"id":"act001472","name":"Möllner Museen, Historisches Rathaus","nameAddition":"Möllner Museen","place":"Mölln","street":"Am Markt 12","ISIL":"DE-MUS-095612","pos":"10.691843843083 53.6305519","teaser":"Stadt- und Gewerbegeschichte","icon":[{"type":"general","id":"opt035"},{"type":"general","id":"opt003"},{"type":"general","id":"opt034"},{"type":"general","id":"opt039"},{"type":"general","id":"opt033"},{"type":"general","id":"opt036"},{"type":"general","id":"opt032"}],"classification":[{"type":"kulturtyp","uri":"http://digicult.vocnet.org/portal/p0090"},{"type":"kulturtyp","uri":"http://digicult.vocnet.org/portal/p-rmkt001"},{"type":"tourismustyp","uri":"http://digicult.vocnet.org/portal/p0297"}],"resource":{"resourceRepresentation":{"type":"image_thumbnail","link":"https://museumsbilder.digicult-verbund.de/thumbnail/m5e905d269ff9e/M%C3%B6llner+Museen%2C+Historisches+Rathaus/M%C3%B6llner+Museum+Au%C3%9Fenansicht"}}}}
    - utter_ask_feedback
* affirm
    - utter_happy
    - utter_anything_else
    - utter_offer_another_tipp
* affirm
    - utter_ask_reset
* affirm
	- slot{"institution": "","institution_name":"","institution_location":"","institution_category":"","institution_tag":""}
    - utter_ask_institution_location
* inform_institution_category{"institution_location":"Flensburg"}
    - slot{"institution_location":"Flensburg"}
    - utter_ask_institution_tag
* inform_institution_tag{"institution_tag":"Familienfreundlich"}
    - slot{"institution_tag":"Familienfreundlich"}
    - action_get_institution
    - utter_ask_feedback
* affirm
    - utter_happy
    - utter_anything_else
    - utter_offer_another_tipp
* deny
    - utter_happy
    - utter_goodbye
* goodbye
    - utter_goodbye
