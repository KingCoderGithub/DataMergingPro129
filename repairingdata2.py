import csv

data = []

with open("data2.csv", "r") as f :
    csvReader = csv.reader(f)
    for row in csvReader :
        data.append(row)
    
headers = data[0]
planetData = data[1:]

# converting all planet names to lowercase
for dataPoint in planetData :
    dataPoint[2] = dataPoint[2].lower()
    
# sorting planet names on the basis of alphabets they start with
planetData.sort(key = lambda planetData : planetData[0])

with open("data2Sort.csv", "a+") as f :
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)
    
