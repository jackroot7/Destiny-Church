import requests
from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values
config = dotenv_values(".env")


class SMSMessage:
    def send_message(sms, receiver):

        data = {
            "source_addr": "DESTINY",
            "encoding": 0,
            "message": sms,
            "recipients": [
                {
                    "recipient_id": 1,
                    "dest_addr": receiver
                }
            ]
        }

        username = config['API_KEY']
        password = config['SECRET_KEY']

        response = requests.post(config['SMS_API'], json=data, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            print("SMS sent successfully!")
        else:
            print("SMS sending failed. Status code:", response.status_code)
            print("Response:", response.text)
        
        
  
        