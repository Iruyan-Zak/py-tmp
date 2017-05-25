class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x + v.x, self.y + v.y)

    def __repr__(self):
        return "Vector2({},{})".format(self.x, self.y)

v1 = Vector2(2,5)
v2 = Vector2(3.5, -1)

v1 += v2

print(v1)
