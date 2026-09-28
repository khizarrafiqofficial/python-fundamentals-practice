class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z,)
    
    def __mul__(self, other):
        result = (self.x * other.x + self.y * other.y + self.z * other.z )
        return result
    
    def __str__(self):
        return f"Vector {self.x}i + {self.y}j + {self.z}k"

v1 = vector(1, 5, 8)
v2 = vector(4, 6, 7)
v3 = vector(9, 3, 2)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)