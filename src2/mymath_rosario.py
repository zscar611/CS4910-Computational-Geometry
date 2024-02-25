# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:52:35 2024

@author: Abdi
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import ConvexHull


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
    
elif option == 3:
    style = 0
    while (style < 1) or (style >2):
        print("Would you like to auto generate points of size (enter '1')")
        print("Or would you like to enter your own points (enter '2')")
        style = int(input())
        
    if style == 1:
        size=0
        while size<3 or size>1000:
            size = int(input("Please enter amount of points you would like to generate(3-1000): "))
        
        pointsList = np.random.randint(0, size, size=(size, 2))  # Random points in 2-D

        hull = ConvexHull(pointsList)

        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(size, 3))

        for ax in (ax1, ax2):
            ax.plot(pointsList[:, 0], pointsList[:, 1], '.', color='k')
            if ax == ax1:
                ax.set_title('Given points')
            else:
                ax.set_title('Convex hull')
                for simplex in hull.simplices:
                    ax.plot(pointsList[simplex, 0], pointsList[simplex, 1], 'c')
                ax.plot(pointsList[hull.vertices, 0], pointsList[hull.vertices, 1], 'o', mec='r', color='none', lw=1, markersize=10)
            ax.set_xticks(range(size))
            ax.set_yticks(range(size))
        plt.show()
    else:
        pointsList = []
        pointsList.append([])
        pointsList.append([])
        point = None
        runs=0
        while point != "stop" and point !=  "Stop" and point !=  "STOP":
            point = input("enter ordered pair(format 'num1,num2') or type stop to end: ")
            if point != "stop" and point != "Stop" and point !=  "STOP":
                x,y = point.split(",")
                int(x)
                int(y)
                pointsList[0].append(x)
                pointsList[1].append(y)
                print(pointsList)
            elif runs < 3:
                point = input("not enough points. enter another")
                x, y = point.split(",")
                int(x)
                int(y)
                pointsList[0].append(x)
                pointsList[1].append(y)
            runs=runs+1
                
        
        
        pointsList = np.array(pointsList)
        pointsList = pointsList.reshape(pointsList.shape[1], pointsList.shape[0])
        hull = ConvexHull(pointsList)

        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(runs, 3))

        for ax in (ax1, ax2):
            ax.plot(pointsList[:, 0], pointsList[:, 1], '.', color='k')
            if ax == ax1:
                ax.set_title('Given points')
            else:
                ax.set_title('Convex hull')
                for simplex in hull.simplices:
                    ax.plot(pointsList[simplex, 0], pointsList[simplex, 1], 'c')
                ax.plot(pointsList[hull.vertices, 0], pointsList[hull.vertices, 1], 'o', mec='r', color='none', lw=1, markersize=10)
            ax.set_xticks(range(runs))
            ax.set_yticks(range(runs))
        plt.show()