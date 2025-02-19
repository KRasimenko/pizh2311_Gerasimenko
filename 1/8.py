class Snow:
    def __init__(self, c):
        self.count = c
    def __add__(self,c):
        self.count+=c
    def __sub__(self,c):
        self.count-=c
    def __mul__(self,c):
        self.count*=c
    def __truediv__(self,c):
        self.count = round(self.count/c)
    def makeSnow(self, row):
        c_row = int(self.count/row)
        s =''
        for i in range(c_row):
            s+= '*' * row + '\n'
        s+=(self.count-c_row*row) * "*"
        if s[-1] == "\n":
            s=s[:-1]
        return s
a = Snow(8)
print(a.makeSnow(4))
