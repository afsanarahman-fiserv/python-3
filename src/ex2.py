import csv

def read_csv(input_file):
    # initialize gym visit counter for input file
    count = 0

    with open(input_file) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        # each "row" is a list of elements in the file line
        for row in rows:
            # skip header row
            if row[0] == "Name":
                continue
            # skip first col (i.e., name)
            for x in range(1, len(row)):
                if int(row[x]) == 1:
                    count += 1

    return count

def find_total_visits():
    count = 0
    count += read_csv("../files/week-1.csv")
    count += read_csv("../files/week-2.csv")
    count += read_csv("../files/week-3.csv")
    return count

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()