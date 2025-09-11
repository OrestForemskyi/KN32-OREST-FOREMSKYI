from datetime import datetime

# Введення імені користувача
name = input("Введіть своє ім'я: ")

# Отримуємо поточний час
current_hour = datetime.now().hour

# Привітання залежно від часу доби
if current_hour < 12:
    greeting = "Доброго ранку"
elif current_hour < 18:
    greeting = "Доброго дня"
else:
    greeting = "Доброго вечора"

# Запитуємо у користувача його вік
age = int(input("Скільки вам років? "))

# Проста логіка: якщо вік < 18, повідомляємо, що ще молодий
if age < 18:
    age_message = "Ви ще молодий!"
else:
    age_message = "Ви вже дорослий!"

# Виводимо результат
print(f"{greeting}, {name}! {age_message} Зараз {datetime.now()}.1")
