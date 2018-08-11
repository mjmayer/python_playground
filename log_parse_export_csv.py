import re
import csv

log = open("apache_logs", "rt").readlines()
rtre = re.compile('(?:HTTP/1\.[10]"\s)(\d{3})')
ipre = re.compile('(^[\d\.]+)(?:\s)')
iprt = []
for l in log:
    ip = ipre.findall(l)[0]
    rt = rtre.findall(l)[0]
    iprt.append( [ip, rt])

with open('csvlog.csv', 'w') as csvfile:
    logwriter = csv.writer(csvfile, delimiter=",")
    for i in iprt:
        logwriter.writerow(i)
