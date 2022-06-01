from flask import Flask, render_template, redirect, request
import json

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")