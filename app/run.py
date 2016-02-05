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
    global runnerUpdateQuery
    runnerUpdateQuery = fr.getRunnerUpdateQuerySet()
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (runnerUpdateQuery, csvOfRun, 1, 196, "delta5", "pwd"))
    return "<h1> Delta 5 is running! </h1>"

@app.route('/caitlin/')
def caitlinRun():
    global csvOfRun
    global runnerUpdateQuery
    runnerUpdateQuery = fr.getRunnerUpdateQuerySet()
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (runnerUpdateQuery, csvOfRun, 1, 196, "cgjohnson4", "pwd"))
    return "<h1> Caitlin is running! </h1>"

@app.route('/frank/')
def frankRun():
    global csvOfRun
    global runnerUpdateQuery
    runnerUpdateQuery = fr.getRunnerUpdateQuerySet()
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (runnerUpdateQuery, csvOfRun, 1, 196, "frank", "pwd"))
    return "<h1> Frank is running! </h1>"

@app.route('/lisa/')
def lisaRun():
    global csvOfRun
    global runnerUpdateQuery
    runnerUpdateQuery = fr.getRunnerUpdateQuerySet()
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (runnerUpdateQuery, csvOfRun, 1, 196, "LisaAMarz", "pwd"))
    return "<h1> Lisa is running! </h1>"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    global runnerUpdateQuery
    runnerUpdateQuery = fr.getRunnerUpdateQuerySet()
    csvOfRun = open('./static/data/fakeRunnersInEv.csv', 'r').readlines()
    app.debug = True
    app.run()
