class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_x(self):
        return self.x
    
    def show_y(self):
        return self.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, p2):
        return ((p2.x - self.x)**2 + (p2.y - self.y)**2)**0.5

p1 = Point(1, 2)
p2 = Point(5, 4)
print(f"\ncoordinate of p1 is ({p1.show_x()}, {p1.show_y()})")
print(f"coordinate of p2 is ({p2.show_x()}, {p2.show_y()})\n")

p1.move(-5, 8)
p2.move(1, -7)
print(f"coordinate of p1 is ({p1.show_x()}, {p1.show_y()})")
print(f"coordinate of p2 is ({p2.show_x()}, {p2.show_y()})\n")

print(f"diastance between p1 and p2 is {p1.dist(p2)}")
