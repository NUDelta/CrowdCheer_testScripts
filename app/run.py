import os
import fakeRunner as fr
import json, httplib
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


@app.route('/stella/')
def stellaRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "fj4WHWBmRr", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/stella_short/')
def stellaShortRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 112, "fj4WHWBmRr", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/caitlin/')
def caitlinRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "cWFnjki325", "cgjohnson4", "pwd"))
    return "<h1> Caitlin is running! </h1>"

@app.route('/frank/')
def frankRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewCheerFromCSV, (csvOfRun, 1, 196, "mRVxiECKyh", "frank", "pwd"))
    return "<h1> Frank is running! </h1>"

@app.route('/lisa/')
def lisaRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewCheerFromCSV, (csvOfRun, 1, 196, "3f0fMYzzEa", "LisaAMarz", "pwd"))
    return "<h1> Lisa is running! </h1>"


#STRESS TESTING

@app.route('/stress20/')
def stressRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "alpha", "pwd"))
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "efXg4Fgwtz", "bravo", "pwd"))
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "QdFwul0E5y", "charlie", "pwd"))
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "fj4WHWBmRr", "delta", "pwd"))
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "2xPmMmDkwF", "echo", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "foxtrot", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "golf", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "hotel", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "india", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "juliet", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "kilo", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "lima", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "mike", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "november", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "oscar", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "papa", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "quebec", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "romeo", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "sierra", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "tango", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "uniform", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "victor", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "whiskey", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "xray", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "yankee", "pwd"))
    # thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "GoNYnHZroG", "zulu", "pwd"))


    return "<h1> Stress Testing: 26 runners are running! </h1>"



if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    csvOfRun = open('./static/data/fakeRunnersInEv.csv', 'r').readlines()
    app.debug = True
    app.run()
