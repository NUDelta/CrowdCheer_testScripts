import os
import fakeRunner as fr
import json, httplib
from flask import Flask,redirect, render_template, json, jsonify, request
import thread, time
app = Flask(__name__)
os.environ["PARSE_API_ROOT"] = "https://crowdcheerdb.herokuapp.com/parse/1"

#NOTE: objectIDs should not be the user ID, but the currRunnerLocation objectID

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
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "HAFXpEDvPk", "stella", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/stella_short/') #bib = 123
def stellaShortRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 112, "HAFXpEDvPk", "stella", "pwd"))
    return "<h1> Stella is running! </h1>"


@app.route('/katherine/') #bib = 456
def katherineRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "hIGE9ttSrw", "katherine", "pwd"))
    return "<h1> Katherine is running! </h1>"


@app.route('/mike/') #bib = 789
def mikeRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "yKibF380Ed", "mike", "pwd"))
    return "<h1> Mike is running! </h1>"


@app.route('/10runners/')
def tenRun():
    with open('./runners.json', 'r') as fp:
        runners = json.load(fp)

        simulateRunner(runners[0], 0, './static/data/fakeRunnerInBelMonEv.csv')

        simulateRunner(runners[1], 0, './static/data/fakeRunnerInEv.csv')
        simulateRunner(runners[2], 0, './static/data/fakeRunnerInEv.csv')

        simulateRunner(runners[3], 25, './static/data/fakeRunnerInEv.csv')
        simulateRunner(runners[4], 25, './static/data/fakeRunnerInEv.csv')

        simulateRunner(runners[5], 45, './static/data/fakeRunnerInEv.csv')
        simulateRunner(runners[6], 45, './static/data/fakeRunnerInEv.csv')

        simulateRunner(runners[7], 65, './static/data/fakeRunnerInEv.csv')
        simulateRunner(runners[8], 65, './static/data/fakeRunnerInEv.csv')
        simulateRunner(runners[9], 65, './static/data/fakeRunnerInEv.csv')

    return "<h1> runners are running! </h1>"

def simulateRunner(runner, delay, csvOfRunPath):

    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open(csvOfRunPath, 'r').readlines()

    print "runner : %s" % runner
    username = runner["username"]
    pwd = runner["pwd"]
    objID = runner["objID"]
    print "runner : %s, objID : %s, username : %s"  % (runner, objID, username)
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, objID, username, pwd, delay))


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
