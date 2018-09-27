
from flask import Flask, render_template, request

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    print(__name__)
    return render_template('auth.html')


@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template('receive.html', username = request.args['username'], method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
