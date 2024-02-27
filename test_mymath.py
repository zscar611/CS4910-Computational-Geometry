from src2.mymath import MyMath

x = MyMath()

def test_shortestdistance():


def test_intersection():

def text_convexHull():
  dataPoints = [[2,4], [3,1], [4,7], [1,9], [10, 12]]
  assert convexHUll() == [[3,1], [2, 4], [1,9], [10, 12]]
  dataPoints = [[1,7], [2,3], [3,3], [4,9], [5, 13]]
  assert convexHUll() == [[1,7], [2, 3], [3, 3], [5, 13]]
  dataPoints = [[0,2], [2,2], [9,12], [13, 17]]
  assert convexHUll() == [[0,2], [2, 2], [13,17]]
