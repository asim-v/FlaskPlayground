## export FLASK_APP=application.py
## export FLASK_ENV=development
from flask import Flask, render_template, request, session 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_session import Session
import datetime
#Variable called session which can be used to store values specific to each user

import csv
import os

#Sessions, init flask
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["FLASK_ENV"] = "development"
app.config["FLASK_DEBUG"] = "1"
Session(app)

#db
engine = create_engine("postgres://nnqbaxqctagpvj:bf5ef956dfd46fafe21aae175693d4454a3e530bde9e82083de4fc81dcf8a06c@ec2-54-165-36-134.compute-1.amazonaws.com:5432/db7900r7fqp39s")#connection string
db = connection = engine.connect()
print(db)

#Request for goodreads api
#gives the review and rating data for the book with the provided ISBN number.
import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Ey8Gn2xOhiJc3Tqsmb2og", "isbns": "9781632168146"})
visible_output=res.json()

    

@app.route('/')#Which page you want to request
def index():#Any name
    now = datetime.datetime.now()
    new_year = now.month  == 1 and now.day == 1
    
    names = ["Cada vez que te veo","B","C",333]
    
    return render_template("index.html",new_year = new_year,names = names)#Only checks templates folder, and looks for the designed variable


@app.route('/david') #Which page you want to request
def david():
    return render_template("more.html")


@app.route('/layout') #Which page you want to request
def layout():
    return render_template("layout.html")

@app.route("/hello", methods=["GET","POST"])#only works for those methods
def hello():
    if request.method == "GET":return "Please submit the form"
    name = request.form.get("name")
    return render_template("hello.html",name=name)

#If he goes into any string dir gets executed
#String directory gets saved as name which can be used as a variable
#@app.route("/<string:name>")
#def respond(name):
#    return f"<h1>hello,{name}<h1>".capitalize()


notes = []

@app.route("/alan", methods=["GET","POST"])
def alan():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)#Only append the note to the specific session
        
    return render_template("evenmore.html",notes=session["notes"])