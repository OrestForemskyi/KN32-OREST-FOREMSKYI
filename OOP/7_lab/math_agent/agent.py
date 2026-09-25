from google.adk.agents.llm_agent import Agent

def calculate_rectangle_area(width: float, height: float) -> float:
    """Обчислює площу прямокутника."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Обчислює площу кола."""
    import math
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """Обчислює об'єм куба."""
    return side ** 3

def calculate_triangle_area(base: float, height: float) -> float:
    """
    Обчислює площу трикутника за основою та висотою.
    
    Args:
        base: довжина основи трикутника
        height: висота трикутника
    """
    return 0.5 * base * height

# Створюємо математичного агента з повним набором інструментів
root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_agent',
    description="Виконує математичні обчислення геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент.
    У тебе є інструменти для обчислення:
    1. Площі прямокутника
    2. Площі кола
    3. Об'єму куба
    4. Площі трикутника (новий інструмент)
    
    Використовуй ці інструменти для розрахунків. 
    Відповідай українською мовою, пиши формулу та пояснюй крок за кроком.
    """,
    tools=[
        calculate_rectangle_area, 
        calculate_circle_area, 
        calculate_cube_volume,
        calculate_triangle_area
    ],
)