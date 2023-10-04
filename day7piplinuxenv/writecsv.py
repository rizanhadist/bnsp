import csv
 
print(csv)

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Marie", "age": 22, "city": "Boston"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]

# Writing CSV files
with open("people.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()  # Write the headers
    for row in data:
        writer.writerow(row)
