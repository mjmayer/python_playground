import requests
import re
import csv

raw_logs = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/apache_logs/apache_logs')
loglines = str(raw_logs.content).strip().split('\\n')

ip_addresses = []
ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
for l in loglines:
    ipmatch = ip.search(l)
    if ipmatch:
        ip_addresses.append([ipmatch.group(0)])

with open('logs.csv', 'w+') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(ip_addresses)
    
