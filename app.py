"""from flask import Flask, render_template, jsonify, make_response
import requests
import json

app = Flask(__name__)

BASE_URL_ACCOUNT = 'https://astrokapoor.com/'
auth_response_details = requests.get(BASE_URL_ACCOUNT)
#response_details = auth_response_details.json()
#response_details_dumps = json.dumps(response_details)
#print(auth_response_details)
print(auth_response_details.text)
#json_response_details = json.dumps(response_details)


@app.route("/html")
def hello():
    return jsonify(response_details_dumps)

@app.route("/hello")
def html():
    return render_template('index.html')"""

from flask import Flask, render_template, jsonify, make_response
import requests
import json

app = Flask(__name__)

def writeToHTMLFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.html'
    with open(filePathNameWExt, 'w') as fp:
        fp.write(data)

path='./'
fileName='example'

BASE_URL_ACCOUNT = 'https://astrokapoor.com/saturn-retrograde-2021/'
auth_response_details = requests.get(BASE_URL_ACCOUNT)
#response_details = auth_response_details.json()
#response_details_dumps = json.dumps(response_details)
#print(auth_response_details)
#print(auth_response_details.text)
#json_response_details = json.dumps(response_details)
writeToHTMLFile('./', fileName, auth_response_details.text)

@app.route("/html")
def hello():
    return "html"

@app.route("/hello")
def html():
    return render_template('index.html')
