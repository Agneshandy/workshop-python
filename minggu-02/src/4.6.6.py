class Point:
    x = int
    y = int

def location(point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")