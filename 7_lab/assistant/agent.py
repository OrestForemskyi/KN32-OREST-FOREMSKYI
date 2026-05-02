from google.adk.agents.llm_agent import Agent

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи зрозумілу історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='assistant_writer',
    description="Збалансований асистент.",
    instruction="""
    Ти корисний асистент. 
    Надавай розгорнуті, зрозумілі та ввічливі відповіді. 
    Дотримуйся балансу між фактами та цікавою подачею.
    """,
    tools=[generate_story_prompt],
    model_config={
        "temperature": 0.7,  # Збалансований режим
        "top_k": 25,
        "top_p": 0.9
    }
)