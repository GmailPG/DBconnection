import csv
path = r'C:\Users\parulgu\Desktop\cust.csv'
with open(path, newline='') as csvfile:
    record = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print(record)
    for row in record:
        print(row)