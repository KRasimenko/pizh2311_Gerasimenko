from Roman_to_int import Roman
from CheckRoman import CheckRoman

class RomanCalculator(Roman, CheckRoman):
   
    def __init__(self):
        """
        Инициализация калькулятора и получение чисел от пользователя. Параметры:
        self: RomanCalculator - объект класса RomanCalculator
        """
        self._number1 = None
        self._number2 = None    
        self.number = None  # для CheckRoman
        self._getNumbers()
    
    def _getNumbers(self):
        """
        Получение чисел от пользователя. Параметры:
        self: RomanCalculator - объект класса RomanCalculator
        """
        self.number = input("Введите первое римское число: ")
        self._number1 = self._setNumber()
        self.number = input("Введите второе римское число: ")
        self._number2 = self._setNumber()
    
    def run(self):
        """
        Запуск калькулятора и обработка операций. После выполнения операции, число преобразуется в римское.
        """
        while True:
            operation = input("Введите операцию (+, -, *, /) или 'q' для выхода. Нажмите 'c' для смены чисел. Нажмите 'p' для вывода чисел: ")
            
            if operation == 'q':
                break
            
            try:
                if operation == '+':
                    result = Roman.__add__(self._number1, self._number2)
                elif operation == '-':
                    result = Roman.__sub__(self._number1, self._number2)
                elif operation == '*':
                    result = Roman.__mul__(self._number1, self._number2)
                elif operation == '/':
                    result = Roman.__truediv__(self._number1, self._number2)
                elif operation == 'p':
                    print(f"Первое число: {self._number1.__str__()}", "Арабское число: ", self._number1.value)
                    print(f"Второе число: {self._number2.__str__()}", "Арабское число: ", self._number2.value)
                    continue
                elif operation == 'c':
                    self._getNumbers()
                    continue
                else:
                    print("Неверная операция. Используйте +, -, *, /")
                    continue
                    
                print(f"Результат: {result}")
                
            except Exception as e:
                print(f"Ошибка: {e}")




