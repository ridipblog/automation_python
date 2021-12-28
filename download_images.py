import requests
import shutil
from bs4 import BeautifulSoup
url="https://www.geeksforgeeks.org/"
reqs=requests.get(url)
soup=BeautifulSoup(reqs.text,'html.parser')
i=0
links=soup.find_all('img')
for link in links:
	urls=link.get('src')
	if ".svg" in urls:
		file="image"+str(i)+".svg"
	else:
		file="image"+str(i)+".jpeg"
	try:
		res=requests.get(urls,stream=True)
	except:
		print("Can't reached to server")
	with open(file,"wb")as file:
		shutil.copyfileobj(res.raw,file)
	i=i+1

