from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

@app.route('/')
def display():
    urllib.urlopen('https://earthengine.googleapis.com/api/thumb?thumbid=0d15ad8d2af6d8d0a6b083672514fae7&token=0604c78c4ea001d93bcc4e89a9b0f4f6')
    return render_template('demo.html', pic=)
