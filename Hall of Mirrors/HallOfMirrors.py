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
"""


def read_hall(file, height):
    primitive_hall = [list(file.readline().rstrip("\n")) for i in range(height)]
    hall = HallOfMirrors()
    for line in primitive_hall:
        hall.add_row(line)
    return hall


def letter_to_cell(letter):
    if letter == "X":
        return SourceCell()
    elif letter == ".":
        return AirCell()
    else:
        return MirrorCell()


def inverse_direction(direction):
    if direction == "NW":
        return "SE"
    elif direction == "N":
        return "S"
    elif direction == "NE":
        return "SW"
    elif direction == "E":
        return "W"
    elif direction == "SE":
        return "NW"
    elif direction == "S":
        return "N"
    elif direction == "SW":
        return "NE"
    elif direction == "W":
        return "E"


class Cell:
    """A generic Hall of Mirrors cell."""
    def __init__(self):
        self.northwest = None
        self.north = None
        self.northeast = None
        self.east = None
        self.southeast = None
        self.south = None
        self.southwest = None
        self.west = None
    
    def propagate_light(self, source_direction, source_coordinates, max_distance):
        pass
    
    def neighbour(self, direction):
        if direction == "NW":
            return self.northwest
        elif direction == "N":
            return self.north
        elif direction == "NE":
            return self.northeast
        elif direction == "E":
            return self.east
        elif direction == "SE":
            return self.southeast
        elif direction == "S":
            return self.south
        elif direction == "SW":
            return self.southwest
        elif direction == "W":
            return self.west
        else:
            assert(False)


class SourceCell(Cell):
    """The cell with the X."""
    def __init__(self):
        Cell.__init__(self)
        self.coordinates = (0, 0)
        self.given_coordinates = []
    
    def propagate_light(self, source_direction, source_coordinates, max_distance):
        if source_direction in ["NW", "NE", "SE", "SW"]:
            self.given_coordinates.append((source_coordinates[0] + 1, source_coordinates[1] + 1))
            # don't propagate
            return
        elif source_direction in ["N", "S"]:
            new_coordinates = source_coordinates[0], source_coordinates[1] + 1
        elif source_direction in ["E", "W"]:
            new_coordinates = source_coordinates[0] + 1, source_coordinates[1]
        # propagate
        inverse = inverse_direction(source_direction)
        self.given_coordinates.append(new_coordinates)
        if new_coordinates[0] ** 2 + new_coordinates[1] ** 2 < max_distance ** 2:
            self.neighbour(inverse).propagate_light(source_direction, new_coordinates, max_distance)
    
    def emit_light(self, max_distance):
        for direction in ["NW", "N", "NE", "E", "SE", "S", "SW", "W"]:
            self.neighbour(direction).propagate_light(inverse_direction(direction), self.coordinates, max_distance)


class AirCell(Cell):
    """A cell with a dot."""
    def __init__(self):
        Cell.__init__(self)
    
    def propagate_light(self, source_direction, source_coordinates, max_distance):
        if source_direction in ["NW", "NE", "SE", "SW"]:
            new_coordinates = source_coordinates[0] + 1, source_coordinates[1] + 1
        elif source_direction in ["N", "S"]:
            new_coordinates = source_coordinates[0], source_coordinates[1] + 1
        elif source_direction in ["E", "W"]:
            new_coordinates = source_coordinates[0] + 1, source_coordinates[1]
        # propagate
        inverse = inverse_direction(source_direction)
        if not new_coordinates[0] ** 2 + new_coordinates[1] ** 2 > max_distance ** 2:
            self.neighbour(inverse).propagate_light(source_direction, new_coordinates, max_distance)


class MirrorCell(Cell):
    """A cell with a number sign (#)."""
    def __init__(self):
        Cell.__init__(self)
    
    def propagate_light(self, source_direction, source_coordinates, max_distance):
        inverse = inverse_direction(source_direction)
        if source_direction in ["NW", "NE", "SE", "SW"]:
            d1, d2 = source_direction
            if isinstance(self.neighbour(d1), MirrorCell) and isinstance(self.neighbour(d2), MirrorCell):
                self.neighbour(source_direction).propagate_light(inverse, source_coordinates, max_distance)
            else:
                # don't propagate the beam
                pass
        elif source_direction in ["N", "E", "S", "W"]:
            self.neighbour(source_direction).propagate_light(inverse, source_coordinates, max_distance)


class HallOfMirrors:
    
    def __init__(self):
        self.rows = []
        self.source = None
        self.number_of_reflections = None
    
    def add_row(self, string):
        assert(not self.rows or len(self.rows[-1]) == len(string))
        self.rows.append([cell for cell in map(letter_to_cell, string)])
        row = self.rows[-1]
        if len(self.rows) == 1:
            row[0].east = row[1]
            row[-1].west = row[-2]
            for i, cell in enumerate(row[1:-1], 1):
                cell.west = row[i - 1]
                cell.east = row[i + 1]
        if len(self.rows) > 1:
            previous_row = self.rows[-2]
            row[0].north = previous_row[0]
            row[0].northeast = previous_row[1]
            row[0].east = row[1]
            row[-1].northwest = previous_row[-2]
            row[-1].north = previous_row[-1]
            row[-1].west = row[-2]
            previous_row[0].southeast = row[1]
            previous_row[0].south = row[0]
            previous_row[-1].southwest = row[-2]
            previous_row[-1].south = row[-1]
            for i, cell in enumerate(row[1:-1], 1):
                cell.northwest = previous_row[i - 1]
                cell.north = previous_row[i]
                cell.northeast = previous_row[i + 1]
                previous_row[i].southwest = row[i - 1]
                previous_row[i].south = cell
                previous_row[i].southeast = row[i + 1]
                cell.west = row[i - 1]
                cell.east = row[i + 1]
                if isinstance(cell, SourceCell):
                    self.source = cell
    
    def emit_light_from_source_and_propagate(self, max_distance):
        self.source.given_coordinates = []
        self.source.emit_light(max_distance)
        self.number_of_reflections = self.count_number_of_reflections(max_distance)
    
    def count_number_of_reflections(self, max_distance):
        result = 0
        for xcoord, ycoord in self.source.given_coordinates:
            if xcoord ** 2 + ycoord ** 2 <= max_distance ** 2:
                result += 1
        return result

