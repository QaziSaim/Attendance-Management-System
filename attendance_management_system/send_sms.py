# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from AMS.models import Student



def SEND_SMS():
    account_sid = "and your api id"
    auth_token =  "Put your account token"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="The Attendance has been taking successfully",
                        from_="enter twilio number",
                        to="Enter Your number"
                    )
    print("message sent sucessfully",message) 