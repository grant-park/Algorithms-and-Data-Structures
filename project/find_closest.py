""" Reads closest pairs input and prints the closest pair as determined by
    the point_set module.
"""

import point_set
import point_pair

def main():
    num_points = int(input())
    points = []
    
    for i in range(num_points):
        # read one line of input, split into x and y, convert to numbers,
        # and add to list
        coords = input().split(" ")
        x = float(coords[0])
        y = float(coords[1])
        points.append((x, y))

    point_pair.print_pair(point_set.closest_pair(points))

if __name__ == '__main__':
    main()
