# William Lu
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-14 W

from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

@app.route('/')
def display():
    x = urllib.request.urlopen('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY')
    str = x.read()
    d = json.loads(str)
    return render_template('demo.html', pic = d['url'])

if __name__ == '__main__':
    app.debug = True
    app.run()
