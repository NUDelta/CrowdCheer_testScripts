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
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "gHQT3H2Cmg", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/stella_short/')
def stellaShortRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 112, "gHQT3H2Cmg", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/caitlin/')
def caitlinRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "cWFnjki325", "cgjohnson4", "pwd"))
    return "<h1> Caitlin is running! </h1>"

@app.route('/moliri/')
def moliriCheer():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeSpectatorInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewCheerFromCSV, (csvOfRun, 1, 261, "VBncWURIbx", "moliri", "pwd"))
    return "<h1> Moliri is cheering! </h1>"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    csvOfRun = open('./static/data/fakeRunnersInEv.csv', 'r').readlines()
    app.debug = True
    app.run()
