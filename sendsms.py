from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT_PHONE_NUMBER, MeSSage 
mess = MeSSage  
def send_sms():
    try:
        # Initialize Twilio Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send SMS
        message = client.messages.create(
            body=mess,  # Message text
            from_=TWILIO_PHONE_NUMBER,  # Twilio phone number
            to=RECIPIENT_PHONE_NUMBER   # Recipient's phone number
        )

        print(f"SMS sent successfully! Message SID: {message.sid}")
    
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# # Example Usage
# if __name__ == "__main__":
#     send_sms("!!! ALERT !!! Unsafe Gesture Detected. Someone is in danger in room 503.")
