""" Этот модуль предназначен для расчета площади
обрабатываемой поверхности и
количества необходимых рулонов обоев """
class WinDoor:
    """Класс для хранения площади прямоугольника, который не
обрабатывается. 
Конструктор задает длину и ширину, объекту присваивается поле "площадь".
"""
    def __init__(self, w, h):
        self.square = w * h
        
class Room:
    """этот класс создает комнаты"""
    def __init__(self, l, w, h):
        """конструктор учитывает размеры помещения"""
        self.length = l
        self.width = w
        self.height = h
        self.wd = []
    def addWD(self, w, h):
        """Метод добавляет объект WinDoor"""
        self.wd.append(WinDoor(w, h))
    def fullSerface(self):
        """Метод высчитывает полную площадь стен"""
        return 2 * self.height * (self.length + self.width)
    def workSurface(self):
        """Этот метод вычисляет площадь
обрабатываемых стен"""
        new_square = self.fullSerface()
        for i in self.wd:
            new_square -= i.square
        return new_square
    def wallpapers(self, l, w):
        """Этот метод определяет количество необходимых рулонов"""
        return int(self.workSurface() / (w * l)) + 1