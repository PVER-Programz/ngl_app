import requests

url = "https://ngl.link/api/submit"
headers = {
	"Host": "ngl.link",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

def ExtractAlnum(string):
	s=""
	for x in string:
		if x in "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_":
			s=s+(x)
	return s

def send(reciever, ques, sender):
	data = {
	"username": reciever,
	"question": ques,
	"deviceId": sender
	}
	response = requests.post(url, headers=headers, data=data)
	return response

reci = input("Reciever id: ")
sendi = ExtractAlnum(reci)
while True:
	ques=input(f"\n[ {reci} <= {sendi} ]\n>>> ")
	if ques!="":
		try:
			resp = send(reci, ques, sendi)
			if resp.json()['questionId'] == None:
				print('User Blocked')
				sendi = input("Sender id: ")
			else:
				print("Message Sent")
		except requests.exceptions.JSONDecodeError as e:
			print("Empty Reciever ID")
		except Exception as e:
			print(type(e), e)
			print("!! Message Not Sent")
	else:
		sendi = input("Sender id: ")
		if sendi=="":
			reci = input("Reciever id: ")
