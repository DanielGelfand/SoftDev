'''Daniel Gelfand
SoftDev1 pd<6>
K<08> -- Solidify
2018-09-21'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print(__name__)
    return "Yo como queso!"

@app.route("/stuy")
def hello_stuy():
    return "GO STUY!"


@app.route("/brooklyn")
def hello_brooklyn():
    return "GO BROOKLYN!"

#app.debug = True

if __name__ == "__main__":
    app.debug = True
    app.run()
