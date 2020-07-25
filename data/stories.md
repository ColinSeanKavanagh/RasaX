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
