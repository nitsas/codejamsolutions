#!/usr/bin/env python3.2
"""
Watersheds problem
for Google Code Jam 2009
Qualification Round
(http://code.google.com/codejam/contest/dashboard?c=90101#s=p1)

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int, read_list_of_int


def get_altitudes_map(file, height):
    altitudes = []
    for i in range(height):
        altitudes.append(read_list_of_int(file))
    return altitudes


def label_cells(altitudes):
    height, width = len(altitudes), len(altitudes[0])
    label_of_cell = [['' for i in line] for line in altitudes]
    unused_labels = label_generator()
    for i in range(height):
        for j in range(width):
            if not label_of_cell[i][j]:
                travel_to_sink_and_label_backwards((i, j), altitudes, label_of_cell, unused_labels)
    return label_of_cell


def travel_to_sink_and_label_backwards(cell, altitudes, label_of_cell, unused_labels):
    path = [cell]
    neighbor = get_lowest_neighbor(altitudes, cell)
    while neighbor:
        # we aren't at the sink yet
        if not label_of_cell[neighbor[0]][neighbor[1]]:
            path.append(neighbor)
            neighbor = get_lowest_neighbor(altitudes, neighbor)
        else:
            label_path(path, label_of_cell, label_of_cell[neighbor[0]][neighbor[1]])
            break
    else:
        # we got to a sink; label the path with a new, unused label
        label_path(path, label_of_cell, next(unused_labels))


def label_generator():
    labels = "abcdefghijklmnopqrstuvwxyz"
    for label in labels:
        yield label


def label_path(path, label_of_cell, label):
    for (i, j) in path:
        label_of_cell[i][j] = label


def get_lowest_neighbor(altitudes, cell):
    row, col = cell
    height, width = len(altitudes), len(altitudes[0])
    lowest_altitude = altitudes[row][col]
    neighbor = ()
    # check North neighbor (if it exists)
    if row > 0 and altitudes[row - 1][col] < lowest_altitude:
        lowest_altitude = altitudes[row - 1][col]
        neighbor = (row - 1, col)
    # now check West neighbor (if it exists)
    if col > 0 and altitudes[row][col - 1] < lowest_altitude:
        lowest_altitude = altitudes[row][col - 1]
        neighbor = (row, col - 1)
    # now check East neighbor (if it exists)
    if col < width - 1 and altitudes[row][col + 1] < lowest_altitude:
        lowest_altitude = altitudes[row][col + 1]
        neighbor = (row, col + 1)
    # finally, check South neighbor (if it exists)
    if row < height - 1 and altitudes[row + 1][col] < lowest_altitude:
        lowest_altitude = altitudes[row + 1][col]
        neighbor = (row + 1, col)
    return neighbor


def print_cell_labels(cell_labels):
    for line in cell_labels:
        print(" ".join(line))


def main():
    if len(sys.argv) != 2:
        print("Usage: runme.py input_file")
        return 1
    with open(sys.argv[1], "r") as f:
        num_maps = read_int(f)
        for i in range(num_maps):
            print("Case #" + str(i+1) + ":")
            (height, width) = read_list_of_int(f)
            altitudes = get_altitudes_map(f, height)
            cell_labels = label_cells(altitudes)
            print_cell_labels(cell_labels)
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

