from InputValidator import InputValidator
class Dumb:
    """Класс для получения стороны квадрата. Создан чтобы продемонстировать принцип наследования"""
    def __init__(self):
        self.side = self.getCurrectSide()

class SnowFlake(Dumb, InputValidator):
    """Класс для создания снежинки"""
    def __init__(self):
        """Инициализирует снежинку. Вызывает метод __init__ родительского класса InputValidator. 
        Параметр side получается из метода getCurrectSide родительского класса InputValidator.
        Результат вызова метода getCurrectSide записывается в атрибут side.
        """
        super().__init__()
        self.snowflakes = self._makeSnow()

    def _checkSnowflakes(self):
        """Проверяет, растаяла ли снежинка.
        Если растаяла, то вызывает метод _makeSnow. 
        В результате снежинка создается заново."""
        if not self.snowflakes:  # Если снежинка растаяла
            self.snowflakes = self._makeSnow()
    
    def _calcSide(self):
        """Считает сторону квадрата. Параметр self.snowflakes является списком строк.
        Длина списка и длина строк в списке равны. В результате возвращается длина списка.
        """
        return len(self.snowflakes)
    
    def _makeSnow(self):
        """Создает снежинку.
        Параметр self.side является стороной квадрата.
        В результате возвращается список строк, каждая из которых состоит из self.side символов "*".
        """
        return ["*" * self.side for _ in range(self.side)]
    
    def thaw(self,s):
        """Растаивает снежинку.
        Параметр s является количеством растаявших снежинок.
        Если количество рядов снежинки меньше 2, то снежинка растаивается. Переменная self.snowflakes становится пустой. Высчитывается новая сторона квадрата.
        Параметр s является количеством строк растаявших снежинок.
        В результате снежинка растаивается на s строк и s символов.
        """
        for _ in range(s):
            if len(self.snowflakes) <=2 or len(self.snowflakes[0]) <=2:
                self.snowflakes = []
                return
            self.snowflakes = self.snowflakes[1:-1]
            self.snowflakes = [line[1:-1] for line in self.snowflakes]
        self.side = self._calcSide()
   
    def freeze(self, n):
        """Замораживает снежинку.
        Параметр n является количеством замороженных снежинок.
        В результате снежинка замораживается на n строк и n символов.
        Вызывается метод _checkSnowflakes.
        В результате снежинка проверяется на растаявшую.
        Параметр current_width является шириной снежинки.
        В результате ширина снежинки увеличивается на 2*n.
        """
        self._checkSnowflakes()
        current_width = len(self.snowflakes[0])
        
        new_line = '*' * (current_width + 2*n)
        for _ in range(n):
            self.snowflakes.insert(0, new_line)
            self.snowflakes.append(new_line)
       
        for i in range(n, len(self.snowflakes)-n):
            self.snowflakes[i] = '*'*n + self.snowflakes[i] + '*'*n
        self.side = self._calcSide()

    def thicken(self):
        """Утолщает снежинку. Параметры self.snowflakes являются списком строк.
        Создается переменная current_width. Она равна длине строк в списке.
        new_line создается из символов "*". Его длина равна current_width.
        В результате снежинка утолщается на 1 символ.
        """
        self._checkSnowflakes()
        current_width = len(self.snowflakes[0])

        new_line = '*' * current_width
        self.snowflakes.insert(0, new_line)
        self.snowflakes.append(new_line)
        for i in range(len(self.snowflakes)):
            self.snowflakes[i] = '*' + self.snowflakes[i] + '*'  
        self.side = self._calcSide()

    def showSnowflakes(self):
        """Выводит снежинку. Параметр self.snowflakes является списком строк.
        В результате выводится снежинка, если она не растаяла. Если растаяла, то выводится сообщение о том, что снежинка растаяла.
        """
        if self.snowflakes:
            print("\n".join(self.snowflakes) + "\n")
        else:
            print("❄️ Снежинка полностью растаяла! ❄️")
    def __call__(self, action=None, amount=1):
        """Делает снежинку вызываемой.
        action: 'thaw' для таяния, 'freeze' для заморозки, 
               'thicken' для утолщения, None для показа
        amount: количество слоев для таяния
        """
        if action == 'thaw':
            self.thaw(amount)
        elif action == 'freeze':
            self.freeze(amount)
        elif action == 'thicken':
            self.thicken()
        else:
            self.showSnowflakes()