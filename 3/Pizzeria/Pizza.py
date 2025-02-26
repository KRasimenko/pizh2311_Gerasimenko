from abc import ABC, abstractmethod

class Pizza(ABC):
    """
    Абстрактный класс для пиццы.
    """
    def __init__(self, name: str, price: float):
        """
        Инициализация пиццы. Параметры:
        name (str): Название пиццы.
        price (float): Цена пиццы.
        """
        self.name = name
        self.price = price
        self.toppings = []
        self.dough = None #тесто
        self.sauce = None 

    def prepare(self):
        """
        Метод для подготовки пиццы.
        """
        print(f"Подготавливаем {self.name}...")
        print(f"Замешиваем {self.dough} тесто...")
        print(f"Добавляем {self.sauce} соус...")
        print("Добавляем топпинги:")
        for topping in self.toppings:
            print(f"- {topping}")

    def bake(self):
        """
        Метод для выпечки пиццы.
        """
        print(f"Выпекаем {self.name}...")

    def cut(self):
        """
        Метод для резки пиццы.
        """
        print(f"Режем {self.name}...")

    def box(self):
        """
        Метод для упаковки пиццы.
        """
        print(f"Упаковываем {self.name}...")

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class PizzaPepperoni(Pizza):
    """
    Класс для пиццы Пепперони.
    """
    def __init__(self):
        super().__init__("Пепперони", 250)
        self.toppings = ["пепперони", "сыр"]
        self.dough = "тонкое"
        self.sauce = "томатный"

class PizzaBarbeque(Pizza):
    """
    Класс для пиццы Барбекю.
    """
    def __init__(self):
        super().__init__("BBQ", 300)
        self.toppings = ["курица", "халапеньо", "сыр"]
        self.dough = "толстое"
        self.sauce = "барбекю"

class PizzaSea(Pizza):
    """
    Класс для пиццы Морская.
    """
    def __init__(self):
        super().__init__("Морская", 350)
        self.toppings = ["сёмга", "креветки", "сыр"]
        self.dough = "тонкое"
        self.sauce = "белый"
    
    
    
    
