import math
def shape_data(name, data1 = 0, data2 = 0):
    if name == "circle":
        perimeter = 2 * math.pi * data1
        area = math.pi * data1 * data1
        print("('C: {:.2f}', 'A: {:.2f}')".format(perimeter, area))
    else:
        perimeter = 2 * (data1 + data2)
        area = data1 * data2
        print("('P: {:.2f}', 'A: {:.2f}')".format(perimeter, area))
shape_data("circle", 15)
shape_data("rectangle", 20, 10)