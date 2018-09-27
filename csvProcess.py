import csv

list = {}

filename = "ADR_Node.csv"
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        list[row[0]] = "ADR"

filename = "Failure_Node.csv"
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        list[row[0]] = "Failure"

filename = "Performance_Node.csv"
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        list[row[0]] = "Performance"

filename = "Re_Node.csv"
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        list[row[0]] = "Re"

filename = "TestCase_Node.csv"
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        list[row[0]] = "TestCase"

filename = "Edge.csv"
data = []
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        if list[row[0]]=="Re" and list[row[1]]=="Re" :
            row[2]="Have"
        elif list[row[0]]=="Failure" and list[row[1]]=="Re" :
            row[2]="Occurs_On"
        elif list[row[0]]=="ADR" and list[row[1]]=="Re" :
            row[2]="Solve"
        elif list[row[0]]=="TestCase" and list[row[1]]=="ADR" :
            row[2]="Verify"
        elif list[row[0]]=="Re" and list[row[1]]=="Performance" :
            row[2]="Indexed_By"
        else:
            row[2]="Unknowned"
        data.append(row)


with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    datatemp = ["From_id","To_id","Type"]
    writer.writerow(datatemp)
    for row in data:
        writer.writerow(row)

print(data)
