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
    #print(raw)
    dict = json.loads(data.decode('utf-8'))
    print(dict)
    return render_template('index.html', desc = dict['title'] ,pic=dict['url'])

if __name__ == '__main__':
    app.debug=True
    app.run()
