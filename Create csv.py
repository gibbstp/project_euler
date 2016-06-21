import csv

def csv_create():
    with open('C:\coding_projects\python_3\project_euler\largest_product_number.txt', 'r') as infile, open('C:\coding_projects\python_3\project_euler\largest_product_number_2.csv', 'w') as outfile:
        my_data = infile.read()
        my_data = my_data.replace('\n', '')
        list = []
        for letter in my_data:
            list.append(int(letter))
        outfile.write(str(list))

csv_create()