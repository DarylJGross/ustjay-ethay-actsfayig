import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

'''
Request Method: POST

use request library to send to the same url  -- Request URL: https://hidden-journey-62459.herokuapp.com/piglatinize/
using the same Request Method: POST
and attaching the input data in the same way "input_text": key  & the fact as value

need to lookup how to attach  form data to a request using request library as the key value pair.


then ultimately you will have to figure out how to retrieve the url from the response I get back from the server....which looks like it is returned as a "location"
key in Response Headers.
'''
# template = """"""

def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()

def get_pig_latin(fact):
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    payload_dict = {'input_text': fact}
    response = requests.post(url, data=payload_dict, allow_redirects=False)
    return response.headers['Location']

@app.route('/')
def home():
    fact = get_fact().strip()
    body = get_pig_latin(fact)

    return Response(response=body, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
