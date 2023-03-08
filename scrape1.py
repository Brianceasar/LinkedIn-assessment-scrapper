# importing the requried library 
import requests
from bs4 import BeautifulSoup as bs

"""
if you are geting the data from the internet use
    data=requests.get('put the url where you are getting the data from')
    
if you are geting the data from a file use
    with open('file.html','r') as f:
        data=f.read()
        
then you need to parse the data using BeautifulSoup as follow
parsed_data=bs(data,'html.parser')
"""

# am getting the data from index.html so am using the second method
with open('index.html','r') as f:
    data=f.read()
    parsed_data=bs(data,"html.parser")

# am finding html tag named <p> and extract the text within it 
data=parsed_data.find("p")

with open("file.txt",'w') as f:
    f.write(data)