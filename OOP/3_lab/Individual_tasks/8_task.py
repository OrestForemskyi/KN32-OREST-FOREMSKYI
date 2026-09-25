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
        """Class property: повертаємо ім’я"""
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property: повертаємо емейл"""
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method"""
        return f"{self.name}@itcollege.lviv.ua"

    @property
    def full_name(self) -> str:
        """Нова властивість: повертає User #id: name (email)"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"


print("Розпочинаємо створювати об’єкти!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This is full_name property: {me.full_name}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
