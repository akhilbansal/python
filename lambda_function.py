import aa


def lambda_handler(event, context):
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return "no match"


def on_intent(intent_request, session):
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "recommendation":
        aa.get_date_by_year(2018)
        return "here are your recommendations"
    elif intent_name == "devicecode":
        return "not yet implemented."
    else:
        return "return from else"
