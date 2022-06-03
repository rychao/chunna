import os
import json
from twilio.rest import Client

account_sid = os.environ['REDACTED']
auth_token = os.environ['REACTED']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+REDACTED',
                              to='1REDACTED'
                          )

# print(message.sid)
