import os
import fakeRunner as fr
import json, httplib
from flask import Flask,redirect, render_template, json, jsonify, request
import thread
app = Flask(__name__)
os.environ["PARSE_API_ROOT"] = "https://crowdcheerdb.herokuapp.com/parse/1"

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


@app.route('/stella/') #bib = 123
def stellaRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "wMHVQT4uak", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/stella_short/') #bib = 123
def stellaShortRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 112, "wMHVQT4uak", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"


@app.route('/katherine/') #bib = 456
def katherineRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "zr6qKr5q7v", "katherine", "pwd"))
    return "<h1> Katherine is running! </h1>"


@app.route('/mike/') #bib = 789
def mikeRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "2FOCUOsUyU", "mike", "pwd"))
    return "<h1> Mike is running! </h1>"


@app.route('/50runners/')
def fiftyRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()

    with open('./runners.json', 'r') as fp:
        runners = json.load(fp)
        for i in runners:
            runner = runners[i]
            objID = runners[i]["objID"]
            username = runners[i]["username"]
            pwd = runners[i]["pwd"]
            print(runner)
            print(objID)
            print(username)
            print(pwd)
            thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, objID, username, pwd))
    return "<h1> runners are running! </h1>"


@app.route('/moliriCheer/')
def moliriCheer():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeSpectatorInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewCheerFromCSV, (csvOfRun, 1, 261, "P8PdmDAQeg", "moliri", "pwd"))
    return "<h1> Moliri is cheering! </h1>"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    csvOfRun = open('./static/data/fakeRunnersInEv.csv', 'r').readlines()
    app.debug = True
    app.run()
