from pprint import pprint

def build_car_list():
    input_lines = []
    with open("../files/input.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            input_lines.append(line.split(","))

    car_ids_lines = []
    with open("../files/car-ids.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            car_ids_lines.append(line.split(","))

    cars = []
    for x in range(1, len(input_lines)):
        line = input_lines[x]
        try:
            car = {'id': int(line[0]), 'miles': int(line[1])}
            cars.append(car)
        except ValueError:
            break

    for line in car_ids_lines:
        id = int(line[0])
        for car in cars:
            if car['id'] == id:
                car['model'] = line[1].strip()
                break

    return cars

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
