# Team C Ya Later -- Jared Asch, William Lu
# SoftDev1 pd7
# K17 -- Average, ... or Basic?
# 2018-10-09 T

import sqlite3   #enable control of an sqlite database

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute('CREATE TABLE peeps_avg (id INTEGER, avg REAL)')

data = c.execute("SELECT * FROM peeps, courses WHERE peeps.id == courses.id;")

idDict = {}
nameDict = {}
for row in data:
    if row[2] in idDict.keys():
        idDict[row[2]].append(row[5])
    else:
        idDict[row[2]] = [row[5]]
    if row[1] not in nameDict.keys():
        nameDict[row[1]] = row[2]

# print(idDict)
print('name,id,average')

for name in nameDict:
    sum = 0
    ctr = 0
    id = nameDict[name]
    for mark in idDict[id]:
        sum += mark
        ctr += 1
    avg = sum / float(ctr)
    print(name + ',' + str(id) + ',' + str(avg))
    c.execute('INSERT INTO peeps_avg VALUES (' + str(id) + ', ' + str(avg) + ');')

db.commit() #save changes
db.close()  #close database
