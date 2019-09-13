# 1 - Sign up on https://www.twilio.com/login
# 2 - Create a twilio free or paid
# 3 - Get AccountSID and aunthentication token

from twilio.rest import Client  # pip install twilio
import requests


account_sid = 'ACed3cbcaed67aa3ba8964b7d3c499fe88'
auth_token = '7ee63f4cca5e54f49b758287de4ee26c'

client = Client(account_sid, auth_token)

# Get api value
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = f'Hi, Fun fact, Number of people in space right now is {str(number_iss)}.'

message = client.messages.create(
    from_='+16233210788',
    to=['+5531975343511'],
    body=Message
)

print(message.sid)
