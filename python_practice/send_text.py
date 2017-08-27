from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6af37aae7d39a8011f17be95ddd526b5"
# Your Auth Token from twilio.com/console
auth_token  = "5658f72ba56436de4b3d9ea6667d5599"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14157267055", 
    from_="+14153267568",
    body="Hello from Python!")

print(message.sid)