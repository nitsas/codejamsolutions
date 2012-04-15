#!/usr/bin/env python3.2
"""
Hall of Mirrors problem
for Google Code Jam 2012
Qualification

Link to problem description:
http://code.google.com/codejam/contest/1460488/dashboard#s=p3

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012

usage:
$ python3.2 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
from math import ceil
# non-standard modules:
from helpful import read_int, read_list_of_int


def read_hall_of_mirrors(file, height, width):
    return [list(file.readline().rstrip("\n")) for i in range(height)]


def explode_hall(hall, max_distance):
    hall = strip_edge_mirrors(hall)
    width = len(hall[0])
    height = len(hall)
    x_position = find_x(hall)[0]
    times = ceil(max_distance / width)
    result, x_position = explode_hall_horizontally(hall, times, x_position)
    times = ceil(max_distance / height)
    result, x_position = explode_hall_vertically(result, times, x_position)
    return result, x_position


def explode_hall_horizontally(hall, times, x_position):
    result = []
    width = len(hall[0])
    for i, line in enumerate(hall):
        result.append(line)
        mirrored_line = line[::-1]
        for k in range(times):
            if k % 2:
                result[i] = line + result[i] + line
            else:
                result[i] = mirrored_line + result[i] + mirrored_line
    x_position = x_position[0], times * width + x_position[1]
    return result, x_position


def explode_hall_vertically(hall, times, x_position):
    hall = transpose(hall)
    x_position = x_position[1], x_position[0]
    result, x_position = explode_hall_horizontally(hall, times, x_position)
    result = transpose(result)
    x_position = x_position[1], x_position[0]
    return result, x_position


def count_reflections(exploded_hall, center, radius):
    result = 0
    x_center, y_center = center
    all_x_positions = find_x(exploded_hall)
    all_x_positions.remove(center)
    rays = []
    for point in all_x_positions:
        if is_close_enough(point, center, radius):
            ray = compute_ray(center, point)
            if ray not in rays:
                # point is not hidden behind another reflection
                result += 1
                rays.append(ray)
    return result


def is_close_enough(point, center, radius):
    if (point[0] - center[0])**2 + (point[1] - center[1])**2 <= radius**2:
        return True
    else:
        return False


def compute_ray(center, point):
    if point[0] == center[0] and point[1] > center[1]:
        return "+Inf"
    elif point[0] == center[0] and point[1] < center[1]:
        return "-Inf"
    else:
        return (point[1] - center[1]) / (point[0] - center[0]), point[0] > center[0]


def strip_edge_mirrors(hall):
    hall = hall[1:-1]
    for i in range(len(hall)):
        hall[i] = hall[i][1:-1]
    return hall


def find_x(hall):
    result = []
    for i, row in enumerate(hall):
        for j, cell in enumerate(row):
            if cell == "X":
                result.append((i, j))
    return result


def transpose(hall):
    return [[hall[i][j] for i in range(len(hall))] for j in range(len(hall[0]))]


def print_hall(hall):
    for line in hall:
        print("".join(line))


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_cases = read_int(f)
        for i in range(1, num_cases + 1):
            height, width, distance = read_list_of_int(f)
            hall = read_hall_of_mirrors(f, height, width)
            exploded, start_position = explode_hall(hall, distance)
            print("Case #{0}: {1}".format(i, count_reflections(exploded, start_position, distance)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

