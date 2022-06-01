from flask import Flask, render_template, redirect, request
import json
from jsondb import JsonDB


"""
import from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
"""


@app.route('/', methods=['GET', 'POST'])

def index():

    return render_template("index.html")

