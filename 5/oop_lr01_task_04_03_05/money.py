import json
from typing import Union
from decimal import Decimal

class LoanCalculator:
    """
    Класс для расчета ежемесячных платежей по кредиту по аннуитетной схеме.
    
    Attributes:
        loan_amount (Decimal): Сумма кредита
        loan_term (int): Срок кредита в месяцах
        interest_rate (Decimal): Годовая процентная ставка
    """
    
    def __init__(self, loan_amount: Union[int, float], 
                 loan_term: int, 
                 interest_rate: Union[int, float]) -> None:
        """
        Инициализация калькулятора кредита.

        Args:
            loan_amount: Сумма кредита
            loan_term: Срок кредита в месяцах
            interest_rate: Годовая процентная ставка в процентах
        """
            
        self.loan_amount = Decimal(str(loan_amount))
        self.loan_term = loan_term
        self.interest_rate = Decimal(str(interest_rate))

    def __add__(self, other: 'LoanCalculator') -> 'LoanCalculator':
        """
        Сложение двух кредитов.
        При сложении:
        - суммы кредитов складываются
        - берется максимальный срок из двух кредитов
        - берется максимальная процентная ставка
        """
        return LoanCalculator(
            float(self.loan_amount + other.loan_amount),
            max(self.loan_term, other.loan_term),
            float(max(self.interest_rate, other.interest_rate))
        )

    def __sub__(self, other: 'LoanCalculator') -> 'LoanCalculator':
        """Разность двух кредитов"""
        return LoanCalculator(
            float(self.loan_amount - other.loan_amount),
            self.loan_term,
            float(self.interest_rate)
        )

    def __str__(self) -> str:
        """Строковое представление кредита"""
        return f"Кредит: {float(self.loan_amount)}₽, {float(self.interest_rate)}%, {self.loan_term} мес."

    @classmethod
    def from_string(cls, str_value: str) -> 'LoanCalculator':
        """
        Создает объект из строки формата "сумма,срок,ставка"
        Пример: "100000,12,7.5" создаст кредит:
        - на сумму 100000
        - сроком на 12 месяцев
        - под 7.5% годовых
        """
        amount, term, rate = str_value.split(',')
        return cls(float(amount), int(term), float(rate))

    def save(self, filename: str) -> None:
        """Сохраняет объект в JSON-файл"""
        data = {
            'loan_amount': float(self.loan_amount),
            'loan_term': self.loan_term,
            'interest_rate': float(self.interest_rate)
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filename: str) -> None:
        """Загружает объект из JSON-файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.loan_amount = Decimal(str(data['loan_amount']))
            self.loan_term = data['loan_term']
            self.interest_rate = Decimal(str(data['interest_rate']))

    def _calculate_monthly_payment(self) -> Decimal:
        """
        Рассчитывает ежемесячный платеж по кредиту.
        
        Formula:
            A = K * (P * (1 + P)^n) / ((1 + P)^n - 1)
            где:
            A - ежемесячный платеж
            K - сумма кредита
            P - месячная процентная ставка (годовая ставка / 12 / 100)
            n - срок кредита в месяцах
        """
        # Расчет месячной процентной ставки (из годовой)
        monthly_rate = self.interest_rate / Decimal('12') / Decimal('100')
        
        # Расчет множителя (1 + P)^n
        temp = (1 + monthly_rate) ** self.loan_term
        
        # Применение формулы аннуитетного платежа
        monthly_payment = self.loan_amount * (monthly_rate * temp) / (temp - 1)
        
        return round(monthly_payment, 2)

    def _get_total_payment(self) -> Decimal:
        """
        Рассчитывает общую сумму выплат по кредиту.

        Returns:
            Decimal: Общая сумма выплат
        """
        monthly_payment = self._calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_term
        return round(total_payment, 2)

    def _get_overpayment(self) -> Decimal:
        """
        Рассчитывает сумму переплаты по кредиту.

        Returns:
            Decimal: Сумма переплаты
        """
        return round(self._get_total_payment() - self.loan_amount, 2)

    def get_payment_schedule(self) -> list[dict]:
        """Возвращает график платежей по месяцам"""
        schedule = []
        # Получаем фиксированный ежемесячный платеж
        monthly_payment = self._calculate_monthly_payment()
        # Начальный остаток долга равен сумме кредита
        remaining_balance = self.loan_amount
        # Расчет месячной процентной ставки
        monthly_rate = self.interest_rate / Decimal('12') / Decimal('100')

        for month in range(1, self.loan_term + 1):
            # Расчет процентной части платежа
            interest_payment = remaining_balance * monthly_rate
            # Расчет части платежа, идущей на погашение тела кредита
            principal_payment = monthly_payment - interest_payment
            # Уменьшаем остаток долга
            remaining_balance -= principal_payment
            
            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),  # Общая сумма платежа
                'principal': round(principal_payment, 2),  # Погашение тела кредита
                'interest': round(interest_payment, 2),  # Проценты
                'remaining': round(max(Decimal('0'), remaining_balance), 2)  # Остаток долга
            })
        
        return schedule