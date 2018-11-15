'''
Daniel Gelfand
SoftDev1 pd6
K#25 -- Getting More REST
2018-11-15 R
'''

import json
from flask import Flask, render_template
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def home():
    response = urlopen('https://api.nasa.gov/planetary/apod?date=2017-11-13&api_key=1kroc6na8JoAYea53lF84EyY8jhmQeL131ptzFBv')
    data = response.read()
    #print(data)
    dict = json.loads(data.decode('utf-8'))

    response1 = urlopen('https://api.adviceslip.com/advice')
    print(response1)
    data1 = response1.read()
    dict1 = json.loads(data1.decode('utf-8'))
    #print(dict1)
    return render_template('index.html', desc = dict['title'] ,pic=dict['url'], advice=dict1['slip']['advice'])

if __name__ == '__main__':
    app.debug=True
    app.run()
