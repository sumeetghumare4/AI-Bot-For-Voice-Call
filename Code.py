import Assembly.AI
from pprint import pprint
# Instantiate the Vonage client object with your API credentials
client = vonage.Client (application_id='2a8d7f05cc4d41c0ad1f1f72618a4ead',private_key="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")

# Create a voice call using the Vonage Voice API
voice = vonage.Voice(client)

response = voice.create_call({
    'to': [{'type': 'phone', 'number': "918055730607"}],
    'from': {'type': 'phone', 'number': "919922682415"},
    'ncco': [{'action': 'talk', 'text': 'Hii candy, Sorry tuzyasathi tu khup chan ahes na nko change tuz behavior'}]
})

pprint(response)






#import vonage as vonage

#voice = vonage.Voice(client)

#response = voice.create_call({
#    'to': [{'type': 'phone', 'number': "919922682415"}],
 #   'from': {'type': 'phone', 'number': "919922682415"},
  #  'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
#})

#pprint(response)