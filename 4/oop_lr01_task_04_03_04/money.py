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

    def _calculate_monthly_payment(self) -> Decimal:
        """
        Рассчитывает ежемесячный платеж по кредиту.

        Returns:
            Decimal: Сумма ежемесячного платежа
            
        Formula:
            A = K * (P * (1 + P)^n) / ((1 + P)^n - 1)
            где:
            A - ежемесячный платеж
            K - сумма кредита
            P - месячная процентная ставка (годовая ставка / 12 / 100)
            n - срок кредита в месяцах
        """
        monthly_rate = self.interest_rate / Decimal('12') / Decimal('100')
        temp = (1 + monthly_rate) ** self.loan_term
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