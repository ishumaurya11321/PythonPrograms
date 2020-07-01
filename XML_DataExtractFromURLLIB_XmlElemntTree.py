# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:22:35 2020

@author: Ishu
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
piece=list()
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    
    print('Retrieved', len(data), 'characters')
    data.decode()
    
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    for item in lst:
        piece.append(item.find('count').text)
        
    print("Count: ",len(piece))
    for i in range(len(piece)):
        piece[i]=int(piece[i])
    print('Sum: ',sum(piece))