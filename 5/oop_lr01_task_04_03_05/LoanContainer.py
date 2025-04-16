import json
from money import LoanCalculator


class LoanContainer:
    def __init__(self):
        """Инициализация пустого контейнера"""
        self._data = []

    def __str__(self):
        """Возвращает строковое представление всех кредитов"""
        if not self._data:
            return "Контейнер пуст."
        return '\n'.join(f"{i}: {str(loan)}" for i, loan in enumerate(self._data))

    def __getitem__(self, index):
        """Позволяет использовать индексацию и срезы"""
        return self._data[index]

    def add(self, value: LoanCalculator):
        """Добавляет объект LoanCalculator в контейнер"""
        if isinstance(value, LoanCalculator):
            self._data.append(value)
        else:
            raise TypeError("Можно добавлять только объекты LoanCalculator.")

    def remove(self, index: int):
        """Удаляет объект по индексу"""
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Индекс вне диапазона.")

    def save(self, filename: str):
        """Сохраняет все кредиты в JSON-файл"""
        data = [{
            'loan_amount': float(loan.loan_amount),
            'loan_term': loan.loan_term,
            'interest_rate': float(loan.interest_rate)
        } for loan in self._data]

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filename: str):
        """Загружает кредиты из JSON-файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            self._data = [LoanCalculator(
                item['loan_amount'],
                item['loan_term'],
                item['interest_rate']
            ) for item in raw_data]
