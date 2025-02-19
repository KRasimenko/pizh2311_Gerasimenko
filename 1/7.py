class Win_Door:
    def __init__(self,x,y):
        self.square = x*y
class Room:
    def __init__(self,w,h,l):
        self.width = w
        self.height=h
        self.lenght = l
        self.wd =[]
    def generalSquare(self):
        return 2*self.height * (self.lenght+self.width)
    def addWD(self,w,h):
        self.wd.append(Win_Door(w,h))
    
    def workSurface(self):
        new_square=self.generalSquare()
        for i in self.wd:
            new_square -=i.square
        return new_square
    def Wallpepers(self,w,h):
        return int(self.workSurface() / (w*h)) + 1
print("Введите параметры вашей комнаты:")
l = float(input("Длина: "))
w = float(input("Ширина: "))
h = float(input("Высота: "))


r1=Room(l,h,w)

flag = input("Есть неоклеиваемая поверхность? (1 - да, 2 - нет)")
while flag== '1':
    w = float(input("Ширина: "))
    h = float(input("Высота: "))
    r1.addWD(w,h)
    flag = input("Добавить еще? (1 - да, 2 - нет)")
print("Размеры рулона: ")
l = float(input("Длина - "))
w = float(input("Ширина - "))
print("Площадь оклейки: ", r1.workSurface())
print("Количество рулонов: ", r1.Wallpepers(l,w))


