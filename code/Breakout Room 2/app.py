from flask import Flask, render_template, redirect, request
import json
import from jsondb import JsonDB

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

