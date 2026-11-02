class Number:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

n1 = Number(7)
n1.check()