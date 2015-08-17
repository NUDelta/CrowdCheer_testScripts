import os
import fakeRunner as fr
from flask import Flask,redirect, render_template, json, jsonify, request
import thread
app = Flask(__name__)
#load the file, make it global
csvOfRun = None
@app.route('/commonality/')
def index():
    ''' This method is going to be where things go that need to happen when someone requests
        the main page
    '''
    users = fr.getAllUsers()
    fr.bDaySims(users)
    fr.computeQuestionSimilarities(users)
    #get the next url
    return "<h1>working</h1>"


@app.route('/fakerun/')
def fakeRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 363))
    return "<h1>Runner is running!</h1>"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    csvOfRun = open('./static/data/fakeRunnerInSF.csv', 'r').readlines()
    app.debug = True
    app.run()
