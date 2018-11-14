'''
Daniel Gelfand
SoftDev1 pd6
K#24 -- A RESTful Journey Skyward
2018-11-14 W
'''

from flask import Flask, render_template
import json
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def home():
    response = urlopen('https://api.nasa.gov/planetary/apod?date=2017-11-13&api_key=1kroc6na8JoAYea53lF84EyY8jhmQeL131ptzFBv')
    data = response.read()
    #print(data)
    dict = json.loads(data.decode('utf-8'))

    response1 = urlopen('https://api.airvisual.com/v2/nearest_city?key=CFqWqyRLZJMMiwDr9')
    data1 = response1.read()
    dict1 = json.loads(data1)
    #print(dict1)
    return render_template('index.html', desc = dict['title'] ,pic=dict['url'], city=dict1['data']['city'], weather = dict1['data']['current']['weather'])

if __name__ == '__main__':
    app.debug=True
    app.run()
