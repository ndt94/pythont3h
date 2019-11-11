class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return abs(self.y2 - self.y1)

    def height(self):
        return abs(self.x2 - self.x1)

    def area(self):
        return self.width() * self.height()


r = Rect(1, 4, 4, 1)
print(r.width())
print(r.height())
print(r.area())
