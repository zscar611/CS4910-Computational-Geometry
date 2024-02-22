import numpy as np
import matplotlib.pyplot as plt
import math


class Segment:
    def __init__(self, start_x,start_y,end_x,end_y):
        self.start_x = float(start_x)
        self.end_x = float(end_x)
        self.start_y = float(start_y)
        self.end_y = float(end_y)
        self.slope = (self.end_y - self.start_y) / (self.end_x - self.start_x)
        self.b = self.end_y - (self.end_x * self.slope)
class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
def swap(x,y):
    return y,x
def distance(p1,p2):
    d = math.sqrt( (abs(p1.x-p2.x))**2 + (abs(p1.y-p2.y))**2 )
    return d
def intersection(seg1,seg2):

    #calculates intersection point
    x_intersect = None
    y_intersect = None
    flag = None

    #if slopes are same no intersection, can avoid divide by zero error
    if(seg1.slope - seg2.slope == 0):
        flag = 1
    else:
        x_intersect = (seg2.b - seg1.b) / (seg1.slope - seg2.slope)
        y_intersect = (seg1.slope * x_intersect) + seg1.b

    #if x intersect is outside the x range of either line
    if not ( (min(seg1.start_x,seg1.end_x) < x_intersect < max(seg1.start_x,seg1.end_x))
              or
              (min(seg2.start_x,seg2.end_x) < x_intersect < max(seg2.start_x,seg2.end_x))  ):
        flag = 1

    # if y intersect is outside the x range of either line
    if not ( (min(seg1.start_y,seg1.end_y) < y_intersect < max(seg1.start_y,seg1.end_y))
              or
              (min(seg2.start_y,seg2.end_y) < y_intersect < max(seg2.start_y,seg2.end_y))  ):
        flag = 1

    #plots both lines
    plt.plot([seg1.start_x,seg1.end_x],[seg1.start_y,seg1.end_y],marker = 'o')
    plt.plot([seg2.start_x, seg2.end_x], [seg2.start_y, seg2.end_y], marker='o')

    #if flag is none plot intersection
    if flag == None:
        plt.plot(x_intersect,y_intersect,'bo')
        print("Intersection at", x_intersect, y_intersect)
    #if not print otherwise
    else:
        print("No Intersection found")

    #show plot
    plt.show()

def shortestdistance(pointsList):
    currentBest = [1000000000000000000,None,None]

    #finding shortest distance
    for x in pointsList:
        for y in pointsList:
            if distance(x,y) != 0 and distance(x,y) < currentBest[0]:
                currentBest[0] = distance(x,y)
                currentBest[1] = x
                currentBest[2] = y


    #plotting all points and a line for the closest 2 points
    for p in pointsList:
        plt.plot(p.x,p.y,'bo')
    plt.plot([currentBest[1].x,currentBest[2].x],[currentBest[1].y,currentBest[2].y])
    print("Shortest distance:",currentBest[0],"between",currentBest[1].x,",",currentBest[1].y,"and",currentBest[2].x,",",currentBest[2].y)
    plt.show()

option = int(input("input 1 for line intersection 2 for shortest distance 3 for convex hull 4 for circle:"))


if option == 1:

    #initialize first segment
    x1, y1 = input("enter ordered pair for line 1 segment start").split(',')
    x2, y2 = input("enter ordered pair for line 1 segment end").split(',')
    if int(x2) < int(x1):
        x1, x2 = swap(x1, x2)
        y1, y2 = swap(y1, y2)
    seg1 = Segment(x1, y1, x2, y2)

    # initialize second segment
    x3, y3 = input("enter ordered pair for line 2 segment start").split(',')
    x4, y4 = input("enter ordered pair for line 2 segment end").split(',')
    if int(x4) < int(x3):
        x3, x4 = swap(x3, x4)
        y3, y4 = swap(y3, y4)
    seg2 = Segment(x3, y3, x4, y4)

    #calculates intersection
    intersection(seg1,seg2)


elif option == 2:

    #generate list of points
    pointsList = []
    point = None
    while point != "stop" and point !=  "Stop" and point !=  "STOP":
        point = input("enter ordered pair or type stop to end")
        if point != "stop" and point != "Stop" and point !=  "STOP":
            x,y = point.split(",")
            pointsList.append(Point(x,y))
        elif len(pointsList) < 3:
            point = input("not enough points. enter another")
            x, y = point.split(",")
            pointsList.append(Point(x, y))
    #calculates shortestdistance
    shortestdistance(pointsList)