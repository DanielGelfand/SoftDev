'''Duckers - Daniel Gelfand and Sophia Xu
SoftDev1 pd<6>
K<10> -- Jinja Tuning
2018-09-24'''

from flask import Flask, render_template
from util import ants
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print(__name__)
    return render_template('test.html', collection = ants.dict,randJob = ants.randJob())


@app.route("/stuy")
def hello_stuy():
    return "GO STUY!"




if __name__ == "__main__":
    app.debug = True
    app.run()
