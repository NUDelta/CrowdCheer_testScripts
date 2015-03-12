import os
from flask import Flask,redirect, render_template, json, jsonify, request

app = Flask(__name__)
#load the file, make it global

@app.route('/similarities/')
def index():
    ''' This method is going to be where things go that need to happen when someone requests
        the main page
    '''
    #get the next url
    return "<h1>working</h1>"


@app.route('/restart/')
def restart():
    return "Restarted!"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
     '''
    app.debug = True
    app.run()
