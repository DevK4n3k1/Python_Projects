##############################################
# Basic Reader (lists)
##############################################
import csv
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    # header = next(reader, None)          # skip header safely (optional)
    for lis in reader:
        print(lis)                       
        # print(lis[0], lis[2])          # by column index


##############################################
# DictReader (dictionary)
##############################################
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for dic in reader:
        print(dic)    
        # print(dic["Product"], dic["Price"])  # by column name


##############################################
# Basic writer (lists → rows)
##############################################
rows = [
    ["Name", "Age", "City"],      # header
    ["Alice", "30", "Auckland"],
    ["Bob", "25", "Wellington"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)        # write multiple rows



##############################################
# DictWriter (dicts → rows, with a header)
##############################################
fieldnames = ["Name", "Age", "City"]
data = [
    {"Name": "Alice", "Age": 30, "City": "Auckland"},
    {"Name": "Bob",   "Age": 25, "City": "Wellington"},
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)


##############################################
# Append
##############################################
new_row = ["Cookie", "2", "1.00"] 

with open("data.csv", "a", newline="", encoding="utf-8") as f: 
    writer = csv.writer(f) 
    writer.writerow(new_row)


##############################################
# Append
##############################################
fieldnames = ["Product", "Quantity", "Price"] 
data = [ 
    {"Product": "Cookie", "Quantity": 2, "Price": "1.00"} 
] 
with open("data.csv", "a", newline="", encoding="utf-8") as f: 
    writer = csv.DictWriter(f, fieldnames=fieldnames) 
    for row in data: 
        writer.writerow(row)