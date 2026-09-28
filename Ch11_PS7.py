class vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = vector([1, 5, 8, 4])
print(len(v1))