import csv

def csv_create():
    with open('Largest product in a series number.txt', 'r') as infile, open('product_series_csv.txt', 'w') as my_csv:
        #my_csv.rstrip(' ')
        for number in infile:
            my_csv.write(number)

csv_create()