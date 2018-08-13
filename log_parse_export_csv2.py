import re
import csv
from pathlib import Path

with Path('apache_logs').open() as f:
    loglines = f.readlines()

r = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:[^"]*")(\w*)(?:[^"]*"\s)(\d{3})')
logparse = []
for l in loglines:
    matches = r.match(l)
    logparse.append([matches.group(1),matches.group(2),matches.group(3)])

with Path('logs.csv').open('w+') as f:
    writer = csv.writer(f, delimiter=',') 
    writer.writerows(logparse)
