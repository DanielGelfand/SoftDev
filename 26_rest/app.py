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
    return render_template('index.html', desc = dict['title'] ,pic=dict['url'])

@app.route('/weather')
def airAPI():
    response = urlopen('https://api.airvisual.com/v2/nearest_city?key=CFqWqyRLZJMMiwDr9')
    data = response.read()
    dict = json.loads(data)
    #print(dict)
    return render_template('air.html', city=dict['data']['city'], weather = dict['data']['current']['weather'])

@app.route('/advice')
def advice():
    response = urlopen('https://api.adviceslip.com/advice')
    #print(response)
    data = response.read()
    dict = json.loads(data.decode('utf-8'))
    #print(dict1)
    return render_template('advice.html',advice=dict['slip']['advice'])




if __name__ == '__main__':
    app.debug=True
    app.run()
