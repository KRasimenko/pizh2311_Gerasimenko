from Pizza import *


class Order:
    """
    Класс для заказа пиццы.
    """
    def __init__(self):
        self.pizzas = []
        self.total_price = 0
    def __str__(self):
        """
        Метод для представления заказа в виде строки. Параметры:
        pizzas (list): Список пицц.
        total_price (float): Сумма заказа.
        """
        return f"Заказ: {self.pizzas} - {self.total_price} руб."
    def add_pizza(self, pizza: Pizza):
        """
        Метод для добавления пиццы в заказ. Параметры:
        pizza (Pizza): Пицца.

        """
        self.pizzas.append(pizza)
        self.total_price += pizza.price
    def remove_pizza(self, pizza: Pizza):
        """
        Метод для удаления пиццы из заказа. Параметры:
        pizza (Pizza): Пицца.
        """
        self.pizzas.remove(pizza)
        self.total_price -= pizza.price
    def get_total_price(self):
        """
        Метод для получения суммы заказа. Параметры:
        total_price (float): Сумма заказа.
        возвращает сумму заказа.
        """
        return self.total_price
    def makeOrder(self):
        """
        Метод для создания заказа.
        параметры:
        pizzas (list): Список пицц.
        total_price (float): Сумма заказа.
        """
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
            print(pizza)
    