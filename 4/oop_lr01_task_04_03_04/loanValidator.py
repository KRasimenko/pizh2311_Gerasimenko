from money import LoanCalculator
from typing import Union


class LoanInterface:
    """
    Класс для взаимодействия с пользователем при расчете кредита.
    Обеспечивает ввод данных с валидацией и вывод результатов.
    """
    
    @staticmethod
    def _get_positive_number(prompt: str) -> Union[int, float]:
        """
        Получает положительное число от пользователя.
        
        Args:
            prompt: Текст приглашения для ввода
            
        Returns:
            Union[int, float]: Введенное пользователем положительное число
            
        Raises:
            ValueError: Если введено некорректное значение
        """
        
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Значение должно быть положительным!")
                    continue
                return value
            except ValueError:
                print("Пожалуйста, введите корректное число!")

    def _get_loan_parameters(self) -> Union[float, int]:
        """
        Запрашивает у пользователя параметры кредита.
        
        Returns:
            Tuple[float, int, float]: Кортеж из суммы кредита, срока и процентной ставки
        """
        loan_amount = self._get_positive_number("Введите сумму кредита: ")
        loan_term = int(self._get_positive_number("Введите срок кредита в месяцах: "))
        interest_rate = self._get_positive_number("Введите годовую процентную ставку: ")
        
        return loan_amount, loan_term, interest_rate

    def _display_results(self, calculator: LoanCalculator) -> None:
        """
        Выводит результаты расчета кредита.
        
        Args:
            calculator: Экземпляр калькулятора кредита с рассчитанными значениями
        """
        monthly_payment = calculator._calculate_monthly_payment()
        total_payment = calculator._get_total_payment()
        overpayment = calculator._get_overpayment()

        print("\nРезультаты расчета кредита:")
        print(f"Сумма кредита: {calculator.loan_amount:,.2f} руб.")
        print(f"Срок кредита: {calculator.loan_term} месяцев")
        print(f"Процентная ставка: {calculator.interest_rate}%")
        print(f"Ежемесячный платеж: {monthly_payment:,.2f} руб.")
        print(f"Общая сумма выплат: {total_payment:,.2f} руб.")
        print(f"Сумма переплаты: {overpayment:,.2f} руб.")

    def run(self) -> None:
        """
        Запускает интерактивный процесс расчета кредита.
        """
        print("Добро пожаловать в кредитный калькулятор!")
        
        while True:
            # Получаем параметры кредита
            loan_amount, loan_term, interest_rate = self._get_loan_parameters()
                
            # Создаем калькулятор и выводим результаты
            calculator = LoanCalculator(loan_amount, loan_term, interest_rate)
            self._display_results(calculator)
                
            # Спрашиваем о продолжении
            if input("\nХотите сделать еще один расчет? (да/нет): ").lower() != 'да':
                print("Спасибо за использование кредитного калькулятора!")
                break
                
                    
    

