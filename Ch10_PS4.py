class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of number is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube of number is {self.n * self.n * self.n}")

    def squareRoot(self):
        print(f"The squareroot of number is {self.n**1/2}")
    @staticmethod
    def greet():
        print("Hello there!")



n = int(input("Enter the number: "))
c = Calculator(n)
c.greet()
c.square()
c.cube()
c.squareRoot()
