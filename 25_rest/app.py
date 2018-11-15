# William Lu
# SoftDev1 pd7
# K25 -- Getting More REST
# 2018-11-15 T

import json, urllib
from flask import Flask, render_template

app = Flask(__name__)

PRE = 'https://dictionaryapi.com/api/v3/references/sd4/json/test?key='
KEY = '1a333d6d-3cd1-4cb2-a2f7-01fe532c946a'
URL = PRE + KEY

@app.route('/')
def display():
    x = urllib.request.urlopen(URL)
    str = x.read()
    d = json.loads(str)
    print(d[0]['meta']['uuid'])
    return render_template('demo.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
