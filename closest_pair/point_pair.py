""" Tools for handling pairs of points. """

import math

def print_pair(p):
    """ Prints the given pair of points in normal form.  Normal form has
        the point with the smaller x-coordinate listed first, with ties broken
        by y-coordinate.
        
        p -- a pair of pairs of numbers
        """
    #closest pair returns three arguments when print pair expects two, so I changed the indices of the arguments
    p1 = p[1]
    p2 = p[2]
    
    if p1[0] < p2[0] or (p1[0] == p2[0] and p1[1] < p2[1]):
        print(p1, "-", p2, "=", point_distance(p1, p2), sep="")
    else:
        print(p2, "-", p1, "=", point_distance(p1, p2), sep="")

def point_distance(p1, p2):
    """ Computes and returns the distance between the two given points.
        
        p1 -- a pair of numbers
        p2 -- a pair of numbers
        """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pair_distance(p1,p2):
    """ Computes and returns the distance between the given pair of points.
        
        p -- a pair of pairs of numbers
        """
    return point_distance(p1, p2)

def closer_than(pair1, pair2):
    """ Determines if the first pair of points is closer than the second.
        The return value will be negative if the first pair is closer,
        positive if the second pair is closer, and 0 if the distances are
        equal.
        
        pair1 -- a pair of pairs of numbers
        pair2 -- a pair of pairs of numbers
        """
        #changed arguments for same reasons as print_pair
    return pair_distance(pair1[0],pair1[1]) - pair_distance(pair2[0],pair2[1]) 