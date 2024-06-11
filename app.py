from flask import Flask,request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

@app.route('/parser', methods=['GET'])
def getElementsInsidePublicRepo():
    urlGithub = request.args.get('url') 
    response = requests.get(urlGithub)
    response.content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the script tag with the specific data-target attribute
    script_tag = soup.find('script', {'data-target': 'react-app.embeddedData'})

    # Get the JSON content from the script tag
    json_content = script_tag.string

    # Parse the JSON content
    data = json.loads(json_content)
    items= data['payload']['tree']['items']
    itemsList=[]
    for d in items:
        itemsList.append(d['name'])
    
    return itemsList
