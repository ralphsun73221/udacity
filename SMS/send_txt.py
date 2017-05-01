from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcac316f6f15db3351f50b5e86f44c7e1"
# Your Auth Token from twilio.com/console
auth_token  = "3b52de627d0dd741cfaab74699c28d33"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8886989907711", 
    from_="+17732956414",
    body="這是一個用來測試用python發送一則SMS的訊息，看到請不要緊張，科科")

print(message.sid)