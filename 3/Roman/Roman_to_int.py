class Roman:
    """
    Класс для работы с римскими числами.
    """
    # Словари для преобразования
    ROMAN_TO_INT = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def __init__(self, roman_numeral: str):
        """
        Инициализация класса Roman. Параметры:
        roman_numeral: str - римское число
        Выполняет:
        - инициализирует атрибут roman_numeral
        - вычисляет значение римского числа
        """
        self.roman_numeral = roman_numeral
        self.value = self._roman_to_int(roman_numeral)

    @staticmethod 
    def _roman_to_int(roman: str) -> int:
        """ Метод для преобразования римского числа в целое число.
        Параметры:
        roman: str - римское число
        Возвращает:
        int - целое число
        """
        result = 0 # Инициализация результата
        prev_value = 0 # Инициализация предыдущего значения
        
        for char in reversed(roman): # Обратный порядок символов
            curr_value = Roman.ROMAN_TO_INT[char] # Получение значения символа
            if curr_value >= prev_value: # Сравнение текущего значения с предыдущим
                result += curr_value # Добавление текущего значения к результату
            else: # Если текущее значение меньше предыдущего
                result -= curr_value # Вычитание текущего значения из результата
            prev_value = curr_value # Обновление предыдущего значения
            
        return result

    @staticmethod
    def _int_to_roman(num: int) -> str:
        """ Метод для преобразования целого числа в римское.
        Параметры:
        num: int - целое число
        Возвращает:
        str - римское число
        """

        int_to_roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        roman = ''
        for value in sorted(int_to_roman_map.keys(), reverse=True):
            while num >= value:
                roman += int_to_roman_map[value]
                num -= value
        return roman


    def __str__(self) -> str:
        """ Метод для преобразования римского числа в строку.
        Возвращает:
        str - римское число
        """
        return self.roman_numeral
    
    def __add__(self, other) -> 'Roman':
        """ Метод для сложения двух римских чисел.
        Параметры:
        other: Roman - римское число
        Возвращает:
        Roman - римское число
        """
        result = self.value + other.value
        return Roman(self._int_to_roman(result))
    def __sub__(self, other) -> 'Roman':
        """ Метод для вычитания двух римских чисел.
        Параметры:
        other: Roman - римское число
        Возвращает:
        Roman - римское число
        """
        result = self.value - other.value
        if result <= 0:
            raise ValueError("Результат не может быть отрицательным или нулевым в римской системе")
        return Roman(self._int_to_roman(result))
    def __mul__(self, other) -> 'Roman':
        """ Метод для умножения двух римских чисел.
        Параметры:
        other: Roman - римское число
        Возвращает:
        Roman - римское число
        """
        result = self.value * other.value
        return Roman(self._int_to_roman(result))
    def __truediv__(self, other) -> 'Roman':
        """ Метод для деления двух римских чисел.
        Параметры:
        other: Roman - римское число
        Возвращает:
        Roman - римское число
        """
        
        result = self.value // other.value 
        if result <= 0:
            raise ValueError("Результат не может быть отрицательным или нулевым в римской системе")
        return Roman(self._int_to_roman(result))
    

