import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.assamcareer.com')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
content=soup.find_all('h1')
i=0
for con in content:
    i=i+1
    print(con.text)
print(i)


# import requests
# from bs4 import BeautifulSoup
# r = requests.get('https://www.assamcareer.com/search?q=nic')
# soup = BeautifulSoup(r.content, 'html.parser')
# content=soup.find_all('h1')
# i=0
# for con in content:
#     i=i+1
#     print(con.text)
# print(i)



# import requests
# headers = {'User-Agent': 'Mozilla/5.0'}
# payload = {'username':'niceusername','password':'123456'}

# session = requests.Session()
# session.post('https://admin.example.com/login.php',headers=headers,data=payload)
# the session instance holds the cookie. So use it to get/post later.
# e.g. session.get('https://example.com/profile')

# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Safari'}
# payload = {'q':'nic'}
# r = requests.post('https://www.assamcareer.com',headers=headers,data=payload)
# soup = BeautifulSoup(r.content, 'html.parser')
# content=soup.find_all('h1')
# print(content[0].text)