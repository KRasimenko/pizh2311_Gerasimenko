class Squere:
    def __init__(self, s, si):
        self.side = int(s)
        self.sign = str(si)
    def __str__(self):
        squr = []
        for i in range(self.side):
            squr.append(self.side*self.sign)
        squr = "\n".join(squr)
        return squr
    def __add__(self, other):
        return Squere(self.side + other.side,self.sign)
a = Squere(5,"S")
b = Squere(5,"T")
c = Squere(5, "V")

print(a)
print(b)
print(c)
print(a+b+c)