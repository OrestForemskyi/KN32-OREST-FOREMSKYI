def check_positive_number(number: int) -> int:
    if number <= 0:
        raise ValueError(f"Число має бути більшим за нуль! Отримано: {number}")
    return number

correct = 15
print(f"Правильне введення ({correct}): {check_positive_number(correct)}")

incorrect = -7
try:
    check_positive_number(incorrect)
except ValueError as e:
    print(f"Неправильне введення ({incorrect}): Помилка -> {e}")