from twilio.rest import Client
import os

# SMS API credentials using environment variable
YOUR_API_SID = os.environ['SMS_API_SID']
YOUR_AUTH_TOCKEN = os.environ['AUTH_TOCKEN']

account_sid = YOUR_API_SID
auth_token = YOUR_AUTH_TOCKEN


# Sent SMS by if weather have possiblity of rain
def smsMachine(sms_body):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=sms_body,
        from_="+15673132761",
        to="+8801521411980"
    )
    print(message.status)
