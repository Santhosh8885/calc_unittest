class Clac:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


    def subtract(self):
        return self.x - self.y


    def multiply(self):
        return self.x * self.y


    def divide(self):
        if self.y == 0:
            raise ValueError('Can not divide by zero!')
        return self.x / self.y

x = Clac(10,20)
print(x.add())
print(x.subtract())
print(x.multiply())
print(x.divide())