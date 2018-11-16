# William Lu
# SoftDev1 pd7
# K26 -- Getting More REST
# 2018-11-16 F

import json, urllib, random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dictionary')
def display():
    PRE = 'https://www.dictionaryapi.com/api/v3/references/sd4/json/'
    WORD = ['extrapolate', 'derivative', 'momentum', 'object']
    MID = '?key='
    KEY = '1a333d6d-3cd1-4cb2-a2f7-01fe532c946a'
    dict = {}
    for word in WORD:
        URL = PRE + word + MID + KEY
        x = urllib.request.urlopen(URL)
        dict[word] = json.loads(x.read())
    # print(list[0][0]['meta'])
    # for word in list:
    #     for d in word:
    #         print(d['meta'])
    return render_template('dict.html', l = dict)

@app.route('/met')
def show():
    PRE = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
    OBJECTS = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
    x = urllib.request.urlopen(OBJECTS)
    full = json.loads(x.read())['objectIDs']
    ID = [random.choice(full), random.choice(full), random.choice(full), random.choice(full), random.choice(full)]
    list = []
    for id in ID:
        URL = PRE + str(id)
        x = urllib.request.urlopen(URL)
        list.append( json.loads(x.read()) )
    return render_template('met.html', l = list)

@app.route('/university')
def list():
    PRE = 'http://universities.hipolabs.com/search?name='
    NAME = 'california'
    URL = PRE + NAME
    x = urllib.request.urlopen(URL)
    list = json.loads(x.read())
    return render_template('university.html', l = list)

@app.route('/iss')
def flex():
    x = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    dict = json.loads(x.read())
    # print(dict)
    return render_template('iss.html', d = dict)


if __name__ == '__main__':
    app.debug = True
    app.run()
