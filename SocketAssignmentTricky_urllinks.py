# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input("Enter Count: ")
pos =  input("Enter Position: ")

#loot thru the count
for i in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving: ", url)
# Retrieve all of the anchor tags
    tags = soup('a')
#Retrieve the new url by choosed position    
    url=tags[int(pos)-1].get('href')
    #print(tag.get('href', None))


#last Retrieved url
print("Retrieving: ", url)