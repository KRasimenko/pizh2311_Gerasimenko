class Rectangle:
    def __init__(self, width, height):
        self.__w = Rectangle.__test(width)
        self.__h = Rectangle.__test(height)
        print(self)
    def setWidth(self,width):
        self.__w = Rectangle.__test(width)
    def getWidth(self):
        return self.__w
    def setHeight(self,height):
        self.__h= Rectangle.__test(height)
    def getHeight(self):
        return self.__h
    def __test(value):
        if value<0:
            return abs(value)
        else:
            return value
    def __str__(self):
        return "Rectangle {0}X{1}".format(self.__w,self.__h)
        
a = Rectangle(5,8)
b = Rectangle(2,6)
a.setHeight(12)
print(a)
