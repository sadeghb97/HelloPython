class Vector :
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, other):
        if isinstance(other, int) :
            return Vector(self.a + other, self.b + other)
        return Vector(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
            return Vector(self.a + other, self.b + other)

v1 = Vector(3, 5)
v2 = Vector(20, 50)
print(v1 + v2)
print(v1 + 100)
print(50 + v1) #agar reverse add ra nemineveshtim inja error midad