class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        tmp = (self.x, self.y)
        return tmp

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __rmul__(self, k: float):
        return Vector(k * self.x, k * self.y)

    def __mul__(self, k: float):
        return self.__rmul__(k)

    def __truediv__(self, k: float):
        return self.__rmul__(1.0 / k)

    def __neg__(self):
        self.x *= -1
        self.y *= -1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_val(self):
        return tuple((self.x, self.y))

    def set_val(self, other):
        if hasattr(other, 'x'):
            self.x = other.x
            self.y = other.y
        else:
            self.x = other[0]
            self.y = other[1]

    value = property(get_val, set_val)
