
import csv
from random import randint
def generate():
    with open('boys.csv', 'w') as csvfile1:
        charnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget', 'Minimum_req']
        w = csv.DictWriter(csvfile1, fieldnames = charnames)
        w.writeheader()
        for i in range (1,50):
            s = {'Name': 'boy'+str(i), 'Attractiveness': randint(1,20), 'Intelligence': randint(1,20), 'Budget': randint(1000,2000), 'Minimum_req': randint(1,10)}
            w.writerow(s)

    with open('girls.csv', 'w') as csvfile2:
        charnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget']
        w = csv.DictWriter(csvfile2, fieldnames=charnames)
        w.writeheader()
        for i in range(1,10):
            s = {'Name': 'girl'+str(i), 'Attractiveness': randint(1,20), 'Intelligence': randint(1,20), 'Budget': randint(1000,2000) }
            w.writerow(s)