import re
import csv

loglines = open('apache_logs').readlines()


hourminute = re.compile('(?:[^\[]*)(?:\[)\d{2}/\w{3}\/\d{4}:(\d{2}:\d{2})')

minutecount = []
for l in loglines:
    minutecount.append(hourminute.search(l).group(1))

logcsv = open('logcsv.csv', 'w+')
csvwrite = csv.writer(logcsv, delimiter=',')
linecount = []
csvlines = []
for m in minutecount:
    if m in linecount:
        pass
    else:
        linecount.append(m)
        csvlines.append([m, minutecount.count(m)])
csvwrite.writerows(csvlines)
logcsv.close()


