class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        self.name = name if name is not None else self.anonymous_user().name
        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        return self.create_email()
    
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name}@{domain}"

    @property
    def full_name(self) -> str:
        """Формат: User #id: name (email)"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

    # ласт модифікація

    def save_to_file(self, filename="users.txt"):
        """Додає рядок із інформацією про користувача у файл"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")
        print(f"Saved {self.full_name} to {filename}")


#тест
print("Розпочинаємо створювати об’єкти!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"{'>'*20}\n{me.full_name}\n{'<'*20}")
    # Зберігаємо у файл
    me.save_to_file("3_lab/Individual tasks/users.txt")
