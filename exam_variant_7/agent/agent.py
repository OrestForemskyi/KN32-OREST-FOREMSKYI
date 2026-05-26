import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

load_dotenv()


class Exercise(ABC):
    def __init__(self, name: str, duration_min: int):
        self.name = name
        self.duration_min = duration_min

    @abstractmethod
    def calories_burned(self) -> float:
        raise NotImplementedError()


class CardioExercise(Exercise):
    def __init__(self, name: str, duration_min: int, intensity: float):
        super().__init__(name, duration_min)
        self.intensity = intensity

    def calories_burned(self) -> float:
        return self.duration_min * 8 * self.intensity


class StrengthExercise(Exercise):
    def __init__(self, name: str, duration_min: int, weight_kg: float):
        super().__init__(name, duration_min)
        self.weight_kg = weight_kg

    def calories_burned(self) -> float:
        return self.duration_min * 5 + self.weight_kg * 0.5


class Workout:
    def __init__(self):
        self.__exercises: list[Exercise] = []

    def add(self, exercise: Exercise):
        self.__exercises.append(exercise)

    def total_calories(self) -> float:
        return sum(ex.calories_burned() for ex in self.__exercises)

    def summary(self) -> dict:
        return {
            "exercises": [
                {"name": ex.name, "calories": ex.calories_burned()} for ex in self.__exercises
            ],
            "total_calories": self.total_calories(),
        }


def calculate_workout(exercises: list) -> dict:
    """
    Інструмент для агента: приймає список словників з полями:
    type: 'cardio' або 'strength', name, duration_min, intensity|weight_kg
    Повертає summary() з Workout.
    """
    workout = Workout()
    for ex in exercises:
        typ = ex.get("type")
        if typ == "cardio":
            workout.add(CardioExercise(ex.get("name"), ex.get("duration_min"), ex.get("intensity")))
        elif typ == "strength":
            workout.add(StrengthExercise(ex.get("name"), ex.get("duration_min"), ex.get("weight_kg")))
    return workout.summary()


SYSTEM_PROMPT = """
Ти — персональний фітнес-тренер. Розраховуй калорії для тренувань і давай рекомендації щодо навантаження.
Коли потрібно порахувати калорії — викликай інструмент `calculate_workout` з переліком вправ.
Відповідай українською мовою.
"""


root_agent = Agent(
    model=os.environ.get("ADK_MODEL", "gemini-3.1-flash-lite"),
    name="FitnessTrainerAgent",
    instruction=SYSTEM_PROMPT,
    description="Персональний фітнес-тренер",
    tools=[calculate_workout],
)
