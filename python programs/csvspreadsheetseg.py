import csv

with open('sa.csv') as csvfile:
  readCSV=csv.reader(csvfile,delimiter=',')

for row in readCSV:
  print(row)

