from ValidationException import ValidationException

def validate_file(file):
    # read file and make each fileline an list element
    lines = []
    with open(file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line)

    # attempt to put car and miles in dictionary
    car_miles = {}
    for x in range(1, len(lines)):
        # note each line should have format "{CarId, (Int)miles}"
        line = lines[x].split(",")
        try:  
            car_miles[int(line[0])] = int(line[1])
        except ValueError:
            raise ValidationException(f"Invalid mileage: {line[1]}")

def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()