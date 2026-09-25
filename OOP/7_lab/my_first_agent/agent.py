import logging
# Імпортуємо інструменти з твого нового модуля
from tools.common_tools import format_text, count_words
from google.adk.agents.llm_agent import Agent

# Налаштування логування для відстеження роботи в консолі
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def logging_tool(param: str) -> dict:
    """
    Інструмент з логуванням подій.
    Дозволяє побачити виклик функції в консолі.
    """
    logger.info(f"--- [LOG] Виклик інструменту logging_tool з параметром: {param} ---")
    return {"result": "success", "processed_param": param}

# Створення агента з повним набором інструментів
root_agent = Agent(
    # Використовуємо модель з робочими квотами зі скріншоту
    model='gemini-3.1-flash-lite-preview', 
    name='multi_tool_agent',
    description="Агент, що використовує спільні інструменти та логування.",
    instruction="""
    Ти технічний помічник. У твоєму розпорядженні є інструменти для:
    1. Форматування тексту (format_text)
    2. Аналізу кількості слів (count_words)
    3. Логування подій (logging_tool)
    
    Завжди використовуй ці інструменти, коли користувач просить обробити текст. 
    Відповідай українською мовою та звітуй про виконані дії.
    """,
    # Додаємо всі імпортовані та локальні функції до списку інструментів
    tools=[format_text, count_words, logging_tool],
)