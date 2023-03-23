class Point:
    def __init__(self, x, y, y1, y2):
        self.x = x
        self.y = y
        self.y1 = y1
        self.y2 = y2

points = [Point(0, 0), Point(1, 1)]

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {points.x}, {points.y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {points.y1}, {points.y2}")
    case _:
        print("Something else")