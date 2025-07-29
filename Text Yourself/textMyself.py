#! python3
#textMyself.py

from twilio.rest import Client

accountSID = 'xxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxx'
myNumber = 'xxxxxxxxxxxxxxxxxxxxxx'
twilioNumber = 'xxxxxxxxxxxxxxxxxxxxxx'

def textMyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body = message,from_ = twilioNumber, to = myNumber)
    
textMyself('Dummy Message')
