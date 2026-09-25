from google.adk.agents.llm_agent import Agent

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи точний технічний опис на тему '{theme}' з {characters} об'єктами."

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='expert_writer',
    description="Експертний аналітик.",
    instruction="""
    Ти суворий експерт-аналітик. 
    Твої відповіді мають бути максимально точними, детермінованими та базуватися лише на фактах.
    Уникай будь-яких художніх засобів чи емоцій.
    """,
    tools=[generate_story_prompt],
    model_config={
        "temperature": 0.1,  # Мінімальна випадковість
        "top_k": 5,
        "top_p": 0.8
    }
)