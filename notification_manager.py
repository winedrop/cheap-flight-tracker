import os
from twilio.rest import Client

TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
USER_PHONE_NUMBER = os.environ.get("USER_PHONE_NUMBER")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)




class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def sendNotification(message: str):
        #sends message in body
        message = client.messages.create(
                                    body=message,
                                    from_=TWILIO_PHONE_NUMBER,
                                    to=USER_PHONE_NUMBER
                                )
        pass
    pass