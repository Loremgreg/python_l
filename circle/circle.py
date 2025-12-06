from point_v1 import Point

point = Point(12, 5)
point.get_x()

point.get_y()


point.set_x(42)
point.get_x()


# Non-public attributes are still accessible
print(point._x)  

print(point._y)  