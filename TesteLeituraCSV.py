import csv

with open("teste.csv") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_reader.__next__()
    for coluna in csv_reader:
        print(coluna[0] + "," + coluna[1] + "," + coluna[2])
