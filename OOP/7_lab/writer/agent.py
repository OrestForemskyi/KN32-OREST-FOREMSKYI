from google.adk.agents.llm_agent import Agent

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи захоплюючу історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='creative_writer',
    description="Креативний письменник історій.",
    instruction="""
    Ти талановитий письменник, який створює захоплюючі історії.
    Твої історії мають бути з несподіваними поворотами сюжету та яскравими персонажами.
    Використовуй багатий словниковий запас та літературні прийоми.
    Відповідай українською мовою.
    """,
    tools=[generate_story_prompt],
    model_config={
        "temperature": 1.3,  # Висока креативність
        "top_k": 40,
        "top_p": 0.95
    }
)