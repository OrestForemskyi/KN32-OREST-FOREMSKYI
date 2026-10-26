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


# 5. Використання маркерів unit та модульної fixture у двох тестах
@pytest.mark.unit
def test_module_fixture_contains_square(module_figures):
    assert "квадрат" in module_figures


@pytest.mark.unit
def test_module_fixture_contains_triangle(module_figures):
    assert "трикутник" in module_figures


# 6. Навмисно зламаний тест
def test_broken_intentionally():
    assert 1 == 2, "Цей тест навмисно зламано для перевірки команди pytest -x"