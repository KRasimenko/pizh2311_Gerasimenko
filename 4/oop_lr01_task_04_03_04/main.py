# Программирование на языке высокого уровня (Python).
# Задание №4. Вариант 6
#
# Выполнил: Герасименко Константин Васильевич
# Группа: ПИЖ-б-о-23-1
# E-mail: kostiktell@mail.ru

from money import LoanCalculator
from loanValidator import LoanInterface

def test_loan_calculator():
    """Тестирование новой функциональности LoanCalculator"""
    # Создание объектов
    credit1 = LoanCalculator(100000, 12, 7.5)
    credit2 = LoanCalculator(50000, 6, 6.5)
    
    print("\n=== Тест специальных методов ===")
    print(f"Кредит 1: {credit1}")
    print(f"Кредит 2: {credit2}")
    
    credit3 = credit1 + credit2
    print(f"Сложение кредитов: {credit3}")
    
    credit4 = credit1 - credit2
    print(f"Разность кредитов: {credit4}")
    
    print("\n=== Тест создания из строки ===")
    credit5 = LoanCalculator.from_string("75000,24,8.5")
    print(f"Создан из строки: {credit5}")
    
    print("\n=== Тест сохранения и загрузки ===")
    credit1.save("credit.json")
    new_credit = LoanCalculator(0, 0, 0)
    new_credit.load("credit.json")
    print(f"Загруженный кредит: {new_credit}")
    
    print("\n=== График платежей (первые 3 месяца) ===")
    schedule = credit1.get_payment_schedule()
    for payment in schedule[:3]:
        print(f"Месяц {payment['month']}: "
              f"Платеж={payment['payment']}₽, "
              f"Основной долг={payment['principal']}₽, "
              f"Проценты={payment['interest']}₽")

if __name__ == "__main__":
    # Запуск тестов функциональности
    test_loan_calculator()
    
    # Запуск интерактивного режима
    print("\n=== Интерактивный режим ===")
    calculator = LoanInterface()
    calculator.run()