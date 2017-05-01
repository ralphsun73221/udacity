from twilio.rest import Client
#from twilio.test import TwilioRestClient
#這是舊版寫法

# Your Account SID from twilio.com/console
account_sid = "ACcac316f6f15db3351f50b5e86f44c7e1"
# Your Auth Token from twilio.com/console
auth_token  = "3b52de627d0dd741cfaab74699c28d33"

#client = TwilioRestClient(account_sid, auth_token)一樣也是舊版的寫法

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886989907711", 
    from_="+17732956414",
    body="這是一個用python撰寫發送一則SMS的程式，看到請不要緊張，科科，絕對不是詐騙喔！！！")

print(message.sid)