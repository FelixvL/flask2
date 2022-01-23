from flask import Flask
import pandas


app = Flask(__name__)

@app.route("/")
def index():    
    return "de flask app commit twee"


@app.route("/twee")
def indexTwee(): 
    pandas.read_csv("Pokemon.csv")   
    return "de flask app commit drie"