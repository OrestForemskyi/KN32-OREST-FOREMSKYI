class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        self.name = name if name is not None else self.anonymous_user().name
        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        """Class property
        return: повертаємо ім’я
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method"""
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"

# написав фунцію
    def name_length(self) -> int:
        """Повертає кількість букв у імені"""
        return len(self.name)


#тест
bohdan = MyName("Bohdan")
print(f"{bohdan.name} має {bohdan.name_length()} букв(и).")

marta = MyName("Marta")
print(f"{marta.name} має {marta.name_length()} букв(и).")
