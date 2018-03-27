import csv
date =csv.reader(open('d:\\testinfo.csv','r'))

for user in date:
    print(user)