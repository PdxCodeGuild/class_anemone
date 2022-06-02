'''
A simple JSON-based database that can be used with Flask.
Usage:
import from jsondb import JsonDB
db = JsonDB('database.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
'''

from flask import Flask, render_template, request, redirect
import nosj

js = nosj.JsonDB()
jsdb = js.load()
todos = js.__getitem__("todos")

x = todos.get('butter the cat')

print(x)