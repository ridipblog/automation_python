# Import libraries
import requests
from bs4 import BeautifulSoup
import wget
# URL from which pdfs to be downloaded
url = "https://www.google.com/search?q=c+pdf&rlz=1C1RLNS_enIN978IN978&oq=c+&aqs=chrome.0.69i59l3j69i60l4j69i65.5707j0j4&sourceid=chrome&ie=UTF-8"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
i = 0
for link in links:
	urls=link.get('href')
	if ".pdf" in urls:
		text=''
		j=0
		while(urls[j]!='&'):
			text=text+urls[j]
			j=j+1
		j=0
		while(text[j]!='h'):
			text=text.replace(text[j],'',1)
		print(text)
		wget.download(text)
print("All PDF files downloaded")
