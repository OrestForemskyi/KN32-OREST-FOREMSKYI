# Звіт до роботи

## Тема: *Тестування з бібліотекою pytest*

### Мета роботи: *Опанувати основи написання модульних тестів за допомогою стороньої бібліотеки pytest, використання фікстур (fixtures) різної області видимості, параметризації тестів, налаштування маркерів та керування залежностями проєкту через Poetry.*

---

## Виконання роботи

### Завдання 1: Ініціалізація проєкту та встановлення залежностей

* Створив конфігурацію проєкту через Poetry та встановив pytest як залежність для розробки.

```bash
poetry init
poetry shell
poetry add --group dev pytest

```

### Завдання 2: Створення основного коду програми

* Створив файл `app.py` із класом `Figure`, який містить перевірки під час ініціалізації та властивості для отримання типу, довжини й кількості кутів фігури.

```python
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: int) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> int:
        return self.length

    @property
    def get_angles(self) -> int:
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        elif self.type == "трикутник":
            return 3
        return 0

```

### Завдання 3: Налаштування маркерів

* Додав конфігурацію для розпізнавання власних маркерів pytest у файл `pyproject.toml`.

```toml
[tool.pytest.ini_options]
markers = [
    "unit: швидкі юніт-тести",
    "slow: повільні тести"
]

```

### Завдання 4: Написання тестів pytest

* Створив файл `test_app.py` та реалізував: параметризацію тестів для коректних і некоректних даних, використання локальних і модульних фікстур, перевірку винятків через `pytest.raises`, а також навмисно зламаний тест для перевірки зупинки виконання.

```python
import pytest
from app import Figure


# 1. Параметризований тест для всіх дозволених фігур
@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figures(figure_type):
    fig = Figure(figure_type, 5)
    assert fig.type == figure_type


# 2. Fixture, яка повертає фігуру з довжиною 10
@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)


def test_fixture_properties(figure_length_10):
    assert figure_length_10.get_figure_length == 10
    assert figure_length_10.get_figure_type == "квадрат"


# 3. Тести для неправильного типу та неправильної довжини
@pytest.mark.parametrize("invalid_type", ["коло", "ромб", "овал"])
def test_invalid_figure_type(invalid_type):
    with pytest.raises(AssertionError):
        Figure(invalid_type, 5)


@pytest.mark.parametrize("invalid_length", [0, -1, -50])
def test_invalid_figure_length(invalid_length):
    with pytest.raises(AssertionError):
        Figure("трикутник", invalid_length)


# 4. Спільна fixture зі scope="module"
@pytest.fixture(scope="module")
def module_figures():
    return Figure.FIGURES


# 5. Використання маркерів unit та модульної fixture
@pytest.mark.unit
def test_module_fixture_contains_square(module_figures):
    assert "квадрат" in module_figures


@pytest.mark.unit
def test_module_fixture_contains_triangle(module_figures):
    assert "трикутник" in module_figures


# 6. Навмисно зламаний тест
def test_broken_intentionally():
    assert 1 == 2, "Цей тест навмисно зламано для перевірки команди pytest -x"

```

### Завдання 5: Виконання тестів та перевірка режимів запуску

- Запуск усіх тестів із детальним виводом (всі тести проходять, крім одного навмисно зламаного).
```bash
pytest -v
```
- Результат виконання коду:
![1 task](/testing/2_lab/pic/1.png)

- Запуск тільки тестів із маркером `unit`.
```bash
pytest -m unit -v
```
- Результат виконання коду:
![2 task](/testing/2_lab/pic/2.png)

- Запуск із зупинкою на першій помилці та коротким виводом трейсбеку.
```bash
pytest -x --tb=short
```
- Результат виконання коду:
![3 task](/testing/2_lab/pic/3.png)
---

## Відповіді на контрольні питання:

#### 1. Команда встановлення pytest через Poetry

```bash
poetry add --group dev pytest

```

#### 2. Різниця між тестом `unittest.TestCase` та функцією `pytest`

* `unittest` вимагає обов'язкового створення класів, що наслідують `TestCase`, та використання спеціальних методів (наприклад, `self.assertEqual()`).
* `pytest` дозволяє писати тести як звичайні функції та використовувати стандартний Python оператор `assert`, що робить код коротшим і простішим. Також `pytest` має потужнішу систему фікстур.

#### 3. Приклад використання параметризації

* Параметризація дозволяє виконати один тест для кількох наборів даних без дублювання коду:

```python
@pytest.mark.parametrize("invalid_length", [0, -1, -50])
def test_invalid_figure_length(invalid_length):
    with pytest.raises(AssertionError):
        Figure("трикутник", invalid_length)

```

#### 4. Приклад використання fixture

* Фікстури використовуються для підготовки об'єктів перед тестом. Тест запитує фікстуру через аргумент із такою ж назвою:

```python
@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)

def test_fixture_properties(figure_length_10):
    assert figure_length_10.get_figure_length == 10

```

#### 5. Приклад використання маркера

* Маркери допомагають об'єднувати тести за призначенням, наприклад, запускати тільки швидкі юніт-тести:

```python
@pytest.mark.unit
def test_module_fixture_contains_square(module_figures):
    assert "квадрат" in module_figures

```

#### 6. Пояснення команди `pytest -x --tb=short`

* Прапорець `-x` вказує зупинити виконання всіх наступних тестів відразу після першої ж знайденої помилки.
* Прапорець `--tb=short` форматує вивід, приховуючи повний стек викликів (traceback) і залишаючи в консолі лише короткий запис про місце збою.

---

### Висновок:

* Що зроблено в роботі;

Опановано фреймворк `pytest`, налаштовано середовище через `Poetry`, реалізовано параметризовані тести, створено фікстури (зокрема зі `scope="module"`) та налаштовано користувацькі маркери для вибіркового запуску тестів.

* Чи досягнуто мети роботи;

Так, мету повністю досягнуто.

* Які нові знання отримано;

Практичні навички написання коротких тестів через функції з використанням `assert`, створення фікстур для підготовки даних, перевірки винятків через `pytest.raises` та використання маркерів для організації тестування.

* Чи вдалось відповісти на всі питання задані в ході роботи;

Так, на всі теоретичні та практичні запитання надано вичерпні відповіді.

* Чи вдалося виконати всі завдання;

Так, усі основні завдання, включаючи спеціальний збій тесту для перевірки аргументів командного рядка, виконано в повному обсязі.

* Чи виникли складності у виконанні завдання;

Виникали проблеми зі шляхами при першому запуску `pytest` та відсутністю змінної оточення у попередній роботі, але перехід у правильну директорію лабораторної та запуск у середовищі Poetry розв'язали проблему.

* Чи подобається такий формат здачі роботи (Feedback);

Так, фіксація завдань у форматі `README.md` зі скриншотами виконання безпосередньо в репозиторії є дуже наочною і зручною.

* Побажання для покращення (Suggestions);

Все чудово!