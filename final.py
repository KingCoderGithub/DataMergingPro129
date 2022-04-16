import csv 

dataset1 = []
dataset2 = []

with open("data1.csv", "r") as f :
    csvReader = csv.reader(f)
    for row in csvReader :
        dataset1.append(row)

with open("data2Sort.csv", "r") as f :
    csvReader = csv.reader(f)
    for row in csvReader :
        dataset2.append(row)

header1 = dataset1[0]
planetData1 = dataset1[1:]

header2 = dataset2[0]
planetData2 = dataset2[1:]

# Merging
headers = header1 + header2
planetData = []
for index, data_row in enumerate(planetData1) :
    planetData.append(planetData1[index] + planetData2[index])

with open("final.csv", "a+") as f :
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)