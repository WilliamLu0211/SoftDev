#Team Johalapenoccupations - William Lu and Puneet Johal
#K10 - Jinja Tuning
#Period 7
#2018-09-23

from flask import Flask, render_template

from util import helper

app = Flask(__name__)

@app.route("/")
def redirect():
    return 'Add "/occupations" to url'

@app.route("/occupations")
def display():
    lines = helper.parse('data/occupations.csv')
    helper.separate(lines)
    jobs = helper.listToDict(lines)
    return render_template("seed.html",
						 title = 'Random occupation generator',
						 head0 = 'Job Class',
                         head1 = 'Percentage',
						 dict = jobs,
						 val = helper.randomJob(jobs))

if __name__ == "__main__":
    app.debug == True
    app.run()
