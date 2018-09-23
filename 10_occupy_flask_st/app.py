from flask import Flask, render_template
import csv, random

app = Flask(__name__)

source = open('occupations.csv', 'rU')
reader = csv.reader(source)

dict = {}
for line in reader:
	dict[line[0]] = line[1]

head0 = 'Job Class'
head1 = dict.pop(head0)

def getKey(dict):
	copy = {}
	for key in dict:
		copy[key] = dict[key]
	copy.pop('Total')
	result = random.random() * 100
	sum = 0
	for key in copy:
		sum += float(copy[key])
		if sum >= result:
			return key

@app.route("/occupations")
def greeting():
	return render_template("seed.html",
							title = 'random occupation generator',
							head0 = head0,
						    head1 = head1,
							dict = dict,
							val = getKey(dict))

app.debug = True
app.run()
