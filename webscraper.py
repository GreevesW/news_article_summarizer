import requests
from bs4 import BeautifulSoup

url = str(input("Enter the website URL: "))
# target url

# making requests instance
reqs = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# stores the text between the body tags of the website in the variable newtext
for body in soup.find_all('body'):
	newtext = body.get_text()

#removes any invalid characters from the text
content = newtext
originalchr = [ chr(34), chr(39), chr(194), "©", chr(92), "&"]
newchr = [ "", "", "", "", "", "and"]

#replaces the invalid characters with the valid alternative in the newchr array
for i in range(0,6):
  content = content.replace( originalchr[i], newchr[i])




#for title in soup.find_all('title'):
	#title = title.get_text()
#print("The title is",title)


#Content is later imported into the chatgpt.py file to be used in the chatgpt prompt
