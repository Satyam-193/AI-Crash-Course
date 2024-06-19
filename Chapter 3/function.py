def distance(x1, x2, y1, y2):
  xy = pow((x1-x2),2) + pow((y1-y2),2)
  result = pow(xy,1/2)
  return result

dis = distance(2,1,4,4)
print(dis)
