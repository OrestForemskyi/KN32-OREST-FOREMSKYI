from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent
from google.adk.agents.llm_agent import Agent

# Використовуємо модель з більшим лімітом (500 запитів/добу)
MODEL = "gemini-3.1-flash-lite"

# --- ЕТАП 1: Паралельний збір даних (Parallel) ---
engine_expert = Agent(
    name="EngineExpert",
    model=MODEL,
    instruction="Ти експерт з двигунів. Опиши сучасний двигун для міського мотоцикла (електро або ДВЗ).",
    output_key="engine_data"
)

design_expert = Agent(
    name="DesignExpert",
    model=MODEL,
    instruction="Ти експерт з дизайну. Опиши стильний зовнішній вигляд для міського байка 2026 року.",
    output_key="design_data"
)

parallel_research = ParallelAgent(
    name="DataGathering",
    sub_agents=[engine_expert, design_expert]
)

# --- ЕТАП 2: Послідовна обробка (Sequential) ---
writer = Agent(
    name="ReportWriter",
    model=MODEL,
    instruction="""
    На основі отриманих даних:
    Двигуни: {engine_data}
    Дизайн: {design_data}
    Склади детальний концепт мотоцикла. Використовуй заголовки та списки.
    Відповідай українською мовою.
    """,
    output_key="report_draft"
)

# Об'єднуємо збір та написання в один ланцюжок
production_pipeline = SequentialAgent(
    name="ProductionPipeline",
    sub_agents=[parallel_research, writer]
)

# --- ЕТАП 3: Цикл покращення (Loop) ---
editor = Agent(
    name="ChiefEditor",
    model=MODEL,
    instruction="""
    Переглянь звіт. Твоя мета — переконатися, що текст якісний та детальний.
    Якщо текст чудовий — виклич exit_loop та поверни його користувачу.
    Якщо він занадто короткий — вкажи, що саме додати, і відправ на повторну генерацію.
    """,
)

# Фінальний агент, який запускає весь процес
root_agent = LoopAgent(
    name="FinalWorkflow",
    sub_agent=production_pipeline,
    exit_loop_tool=editor
)