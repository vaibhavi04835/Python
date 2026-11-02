class Largest:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_largest(self):
        if self.a >= self.b and self.a >= self.c:
            print("Largest Number:", self.a)
        elif self.b >= self.a and self.b >= self.c:
            print("Largest Number:", self.b)
        else:
            print("Largest Number:", self.c)

l1 = Largest(10, 25, 15)
l1.find_largest()