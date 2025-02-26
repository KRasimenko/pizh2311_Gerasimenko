from Order import Order
from Pizza import PizzaPepperoni, PizzaBarbeque, PizzaSea

class Terminal:
    """
    Класс для терминала.
    """
    PIZZA_MENU = {
        "1": {"name": "Пепперони", "price": 250, "class": PizzaPepperoni},
        "2": {"name": "BBQ", "price": 300, "class": PizzaBarbeque},
        "3": {"name": "Морская", "price": 350, "class": PizzaSea}
    }

    def __init__(self):
        self.order = Order()
        self.ordered_pizzas = []
        self.order_counter = 0
        
    def __str__(self):
        """Возвращает информацию о текущем состоянии терминала"""
        if not self.ordered_pizzas:
            return "Заказ пуст"
        return f"Заказ №{self.order_counter}\nЗаказанные пиццы: {', '.join(str(pizza) for pizza in self.ordered_pizzas)}"
    
    def show_menu(self):
        """Показывает меню пользователю"""
        print("Добро пожаловать в СкфуПицца!\n=== Меню ===")
        print("1. Добавить пиццу в заказ")
        print("2. Показать текущий заказ")
        print("3. Оплатить заказ")
        print("4. Выход")
        
        
    def show_pizza_menu(self):
        """Показывает меню пицц"""
        print("\n=== Виды пицц ===")
        for key, pizza in self.PIZZA_MENU.items():
            print(f"{key}. {pizza['name']} - {pizza['price']} руб")
    
    def add_pizza_to_order(self, pizza_choice):
        """Добавляет выбранную пиццу в заказ"""
        if pizza_choice in self.PIZZA_MENU:
            pizza_data = self.PIZZA_MENU[pizza_choice]
            pizza = pizza_data["class"]()  # Создаем объект пиццы
            self.ordered_pizzas.append(pizza)
            self.order.add_pizza(pizza)
            print(f"Пицца {pizza_data['name']} добавлена в заказ")
        else:
            print("Неверный выбор пиццы")

    def calculate_total(self):
        """Вычисляет общую сумму заказа"""
        return self.order.get_total_price()

    def process_command(self, choice):
        """Обрабатывает команду пользователя"""
        if choice == "1":
            self.show_pizza_menu()
            pizza_choice = input("Выберите пиццу (1-3): ")
            self.add_pizza_to_order(pizza_choice)
        elif choice == "2":
            print("\nТекущий заказ:")
            print(self)
        elif choice == "3":
            if self.ordered_pizzas:
                self.process_payment()
            else:
                print("\nНевозможно оплатить пустой заказ")
        elif choice == "4":
            return False
        return True
    
    def process_payment(self):
        """Обрабатывает оплату заказа. Параметры:
        total (int): Сумма заказа.
        """
        total = self.calculate_total()
        print(f"\nСумма к оплате: {total} руб")
        
        try:
            payment = int(input("Введите сумму для оплаты: "))
            if payment >= total:
                self.order_counter += 1
                print(f"Оплата принята. Сдача: {payment - total} руб")
                print("\nГотовим ваш заказ...")
                for pizza in self.ordered_pizzas:
                    pizza.makeOrder()
                    print("")  # Пустая строка для разделения пицц
                print("Заказ оформлен!")
                self.ordered_pizzas = []
                self.order = Order()
            else:
                print("Недостаточно средств")
        except ValueError:
            print("Введите корректную сумму")

    def run(self):
        """Запускает основной цикл работы терминала. Параметры:
        choice (str): Выбор пользователя.
            """
        while True:
            self.show_menu()
            choice = input("\nВыберите действие (1-4): ")
            if not self.process_command(choice):
                break
