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
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "wl7DOoTpKR", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"

@app.route('/stella_short/') #bib = 123
def stellaShortRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv_short.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 112, "wl7DOoTpKR", "delta", "pwd"))
    return "<h1> Stella is running! </h1>"


@app.route('/caitlin/') #bib = 456
def caitlinRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "JkdEbqbNpg", "cgjohnson4", "pwd"))
    return "<h1> Caitlin is running! </h1>"


@app.route('/moliriRun/') #bib = 789
def moliriRun():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeRunnerInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewRunFromCSV, (csvOfRun, 1, 196, "B50jwtYerd", "", "pwd"))
    return "<h1> Moliri is running! </h1>"


@app.route('/moliriCheer/')
def moliriCheer():
    global csvOfRun
    if csvOfRun == None:
        csvOfRun = open('./static/data/fakeSpectatorInEv.csv', 'r').readlines()
    thread.start_new_thread(fr.fakeNewCheerFromCSV, (csvOfRun, 1, 261, "L8wbhmf3al", "moliri", "pwd"))
    return "<h1> Moliri is cheering! </h1>"

if __name__ == "__main__":
    ''' This is where stuff goes that will need to run when the server is started
    '''
    global csvOfRun
    csvOfRun = open('./static/data/fakeRunnersInEv.csv', 'r').readlines()
    app.debug = True
    app.run()
