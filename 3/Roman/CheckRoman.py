from Roman_to_int import Roman
class CheckRoman:
    def _isRoman(self, roman: str) -> bool:
        """ Метод для проверки, является ли строка римским числом.
        Параметры:
        roman: str - римское число
        Возвращает:
        bool - True, если строка является римским числом, иначе False
        """
        if roman.isdigit():
            return False
            
        for char in roman:
            if char.upper() not in self.ROMAN_TO_INT:
                return False
        return True
    
    def _setNumber(self) -> str:
        """
        Проверка и установка римского числа. Параметры:
        self: CheckRoman - объект класса CheckRoman
        Возвращает:
        Roman - объект класса Roman
        """
        while not self._isRoman(self.number):
            self.number = input("Неверный формат. Введите римское число: ")
        return Roman(self.number.upper())
   