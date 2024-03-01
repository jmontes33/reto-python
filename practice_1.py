import csv
import pandas as pd

csv_file = 'reto.csv'

with open(csv_file) as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)