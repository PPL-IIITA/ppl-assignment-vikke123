import csv
from vicky import Boy,Girl
from generate import generate
from log import logging

getgirl = []
getboy = []

with open('girls.csv','r') as csvfile2:
    r = csv.DictReader(csvfile2)
    for row in r:
        getgirl.append(Girl(row['Name'], row['Attractiveness'], row['Intelligence'], row['Budget']))

with open('boys.csv','r') as csvfile1:
    r = csv.DictReader(csvfile1)
    for row in r:
        getboy.append(Boy(row['Name'], row['Attractiveness'], row['Intelligence'], row['Minimum_req'], row['Budget']))
for i in getgirl:
    for j in getboy:
        logging.info('is checking to ' + i.name + ' with ' + j.name)
        if (i.checkElligible(j) and j.checkElligible(i) ):
            j.rstatus = 'commited'
            i.rstatus = 'commited'
            j.girlfriend = i.name
            i.boyfriend = j.name
            logging.info('Is commited to ' +  i.name + ' with ' + j.name)
            break

for x in getgirl :
    if x.rstatus != 'single':
        print(x.name + ' is a commited to: ' + x.boyfriend)
    else:
        print(x.name + ' is single ')