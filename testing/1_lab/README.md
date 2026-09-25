# Звіт до роботи
## Тема: _Загальне тестування та юніт-тести за допомогою unittest_
### Мета роботи: _Опанувати основи перевірки даних (assert, винятки) та навчитися писати модульні тести для функцій і класів у Python з використанням бібліотеки unittest, зокрема для граничних значень, з параметризацією через subTest та підміною введення за допомогою mock._

---
## Виконання роботи
### Завдання 1: Перевірка введеного числа
* Реалізував перевірку додатного числа за допомогою винятку ValueError та перевірив роботу для правильного й неправильного значень.
``` python 
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
```
* Результат виконання коду:
![1 task](/testing/1_lab/pic/1task.png)
 ### Завдання 2: Тестування функцій

* Створив функцію підрахунку голосних літер (з підтримкою українського та латинського алфавітів) і написав юніт-тести для звичайного рядка, порожнього значення, рядка з цифрами та тексту українською мовою.

```python
import unittest


def count_vowels(text: str) -> int:
    vowels = set("аеєиіїоуюяaeiouАЕЄИІЇОУЮЯAEIOU")
    return sum(1 for char in text if char in vowels)


class TestCountVowels(unittest.TestCase):
    def test_standard_string(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_digits_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#"), 0)

    def test_ukrainian_letters(self):
        self.assertEqual(count_vowels("Привіт світ"), 3)
        self.assertEqual(count_vowels("Яблуко"), 3)


if __name__ == "__main__":
    unittest.main()

```

* Результат виконання коду:
![2 task](/testing/1_lab/pic/2task.png)
### Завдання 3: Робота з класом Figure та його тестування

* Додав метод `get_angles` у клас `Figure` та написав тести для кутів, граничних довжин (0, від'ємні значення) і некоректного типу фігури.

#### Код який я дописав в `app.py`:
```python
@property
    def get_angles(self) -> int:
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        elif self.type == "трикутник":
            return 3
        return 0
```
#### Код який я дописав в `test.py`:
1. Додаткові об'єкти в метод setUp
```python
        self.rectangle = Figure("прямокутник", 10)
        self.triangle = Figure("трикутник", 3)
```
2. Нові методи тестів (всередину класу TestFigure):
```python
def test_get_angles(self):
        self.assertEqual(4, self.square.get_angles)
        self.assertEqual(4, self.rectangle.get_angles)
        self.assertEqual(3, self.triangle.get_angles)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("трикутник", -5)
```
* Результат виконання коду:
![3 task](/testing/1_lab/pic/3task.png)

Ось оформлення для цих завдань у твоєму форматі:

### Завдання 4: Використання subTest для перевірки всіх типів Figure

* Додав тест із параметризацією за допомогою `subTest` для перевірки створення та кількості кутів для кожного допустимого типу фігури (`квадрат`, `прямокутник`, `трикутник`).

```python
import unittest
from app import Figure


class TestFigureSubTest(unittest.TestCase):
    def test_all_figure_types(self):
        figures_data = [
            ("квадрат", 4),
            ("прямокутник", 4),
            ("трикутник", 3),
        ]
        for fig_type, expected_angles in figures_data:
            with self.subTest(figure_type=fig_type):
                fig = Figure(fig_type, 5)
                self.assertEqual(fig.get_figure_type, fig_type)
                self.assertEqual(fig.get_angles, expected_angles)


if __name__ == "__main__":
    unittest.main(verbosity=2)

```

* Результат виконання коду:
![4 task](/testing/1_lab/pic/4task.png)

---

### Завдання 5: Тестування функції з input() за допомогою unittest.mock

* Створив функцію привітання користувача з викликом `input()` та протестував її без ручного введення за допомогою декоратора `@patch` із `unittest.mock`.

```python
import unittest
from unittest.mock import patch


def greet_user() -> str:
    name = input("Введіть ваше ім'я: ")
    return f"Привіт, {name}!"


class TestGreetUser(unittest.TestCase):
    @patch("builtins.input", return_value="Орест")
    def test_greet_user(self, mock_input):
        result = greet_user()
        self.assertEqual(result, "Привіт, Орест!")
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)

```

* Результат виконання коду:
![5 task](/testing/1_lab/pic/5task.png)


---

## Відповіді на контрольні питання:

#### 1. Команди запуску

```bash
python test.py
python -m unittest -v

```

#### 2. Тест, що не проходив, та результат після виправлення

* **Помилка до виправлення:** тест `test_get_angles` падав з помилкою `AttributeError: 'Figure' object has no attribute 'get_angles'` через відсутність реалізації властивості в класі `Figure`.


* **Виправлення:** у клас `Figure` додано властивість:

```python
@property
def get_angles(self) -> int:
    if self.type in ["квадрат", "прямокутник"]:
        return 4
    elif self.type == "трикутник":
        return 3
    return 0

```

* **Результат:** усі тести виконано успішно (`Ran 6 tests ... OK`).

#### 3. Призначення subTest та mock

* **`subTest`**: дозволяє тестувати кілька наборів даних у межах одного методу тесту; якщо один випадок завершиться помилкою, інші все одно будуть перевірені.
* **`unittest.mock` (`patch`)**: підміняє зовнішні залежності (наприклад, функцію `input()`) заздалегідь визначеним значенням, забезпечуючи автоматичне виконання тесту без участі користувача.


## Звіт виконаної роботи на лекціях

* Перевірка через `if-else`: ручний аналіз результатів із викликом винятку `AssertionError`.
* Оператор `assert`: базова перевірка умови в коді; не є повноцінним тестом, але використовується для внутрішніх валідацій.
* Фреймворк `unittest`: стандартна бібліотека Python для побудови структурованих тестів у класах, що наслідують `unittest.TestCase`.


* **Методи перевірки `unittest`:**
* `assertEqual(a, b)` — перевірка рівності значень.
* `assertIsInstance(a, type)` — перевірка типу об'єкта.
* `assertAlmostEqual(a, b)` — порівняння чисел із плаваючою крапкою (`float`) із заданою точністю.


* **Параметризація через `subTest`:**
* Використання контекстного менеджера `with self.subTest(...)` дозволяє проходити масив тестових наборів (кортежів значень) в одному методі тесту, не перериваючи виконання при невдачі одного з випадків.


* **Життєвий цикл тестового класу (`Fixtures`):**
* `setUp()` — виконується перед кожним окремим тест-методом (створення та ініціалізація об'єкта `SimpleClass`).
* `tearDown()` — виконується після кожного тесту (очищення ресурсів або видалення створених об'єктів).


* **Структура проєкту:**
* Розділення вихідного коду програми (`src/lab1/`) та юніт-тестів (`tests/test_main.py`) із керуванням залежностями через `pyproject.toml` (Poetry).










---
### Висновок:

* Що зроблено в роботі;

Опановано валідацію даних через винятки та `assert`, реалізовано модульні тести для функцій і класів у `unittest`, застосовано параметризацію `subTest` та макетування за допомогою `unittest.mock.patch`.
* Чи досягнуто мети роботи;

Так, мету повністю досягнуто.
* Які нові знання отримано;

Практичні навички написання юніт-тестів на Python, використання тестових фікстур (`setUp`, `tearDown`), ізоляції залежностей через `mock` та пакетної перевірки даних через `subTest`.
* Чи вдалось відповісти на всі питання задані в ході роботи;

Так, на всі теоретичні та практичні запитання надано вичерпні відповіді.
* Чи вдалося виконати всі завдання;

Так, усі основні та додаткові завдання виконано в повному обсязі.
* Чи виникли складності у виконанні завдання;

Серйозних труднощів не було; виникали лише дрібні помилки під час запуску через незбережені зміни у файлах, які було одразу виправлено.
* Чи подобається такий формат здачі роботи (Feedback);

Так, фіксація завдань у форматі `README.md` зі скриншотами виконання безпосередньо в репозиторії є дуже наочною і зручною.
* Побажання для покращення (Suggestions); 

Все прекрасно!
