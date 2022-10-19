import csv


lines_to_skip = 3
file = "/Users/garybannon/Desktop/Intro to PP/Exercises week 5/customers.csv"

file_reader = open(file, "r")
read_file = csv.DictReader(file_reader, delimiter=',', quotechar='"')

for _ in range(lines_to_skip):
    file_reader.readline()
    continue

for row in read_file:
    print(row)




