import random

#parse through the csv file
def parse(inputfile):
    file = open(inputfile, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    return raw.split("\n")      #split on new lines + return list of lines

#separate jobs from percentages
def separate(inputlist):
    index = 0
    while index < len(inputlist):
        if '"' in inputlist[index]:
            inputlist[index] = inputlist[index].replace('"', '') #remove extra quotes
        inputlist[index] = inputlist[index].rsplit(',', 1) #split at last comma in line (the one before the percetage)
        index += 1

#feed info into dictionary
def listToDict(inputlist):
    jobs = {}
    line = 1 #skips table header
    while line < (len(inputlist) - 2):
        jobs[inputlist[line][0]] = float(inputlist[line][1]) #Each even index element (job) becomes a key, and the odd index element right after it becomes the value
        line += 1
    return jobs

#random job selection
def randomJob(dictionary):
    keys = list(dictionary) #returns list of all keys in dict
    return random.choice(keys)
