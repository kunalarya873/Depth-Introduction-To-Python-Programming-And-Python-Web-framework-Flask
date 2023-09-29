from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello_world():
   return "<h1>Hello World</h1>"

@app.route('/welcome/<name>')
def welcome_name (name):
           return 'Welcome to the Website'+name+ ' !'

if __name__ == "__main__":
   app.run(debug = True)