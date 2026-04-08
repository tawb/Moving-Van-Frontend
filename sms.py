from twilio.rest import Client
import os

account_sid = os.environ.get('AC10c27444d032f664c9d1c454c4fdd301')
auth_token = os.environ.get('7af795bfdbecf420766079e77baba02c')

client = Client(account_sid, auth_token)


message = client.messages.create(
    from_='+12254354848',  
    body='hi',
    to='970568172682'  
)




print(message.sid)