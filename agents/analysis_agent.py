"""
Enterprise Strategic Agent for AI Business Assistant
LangChain modern API + Groq + Automatic Insights Generation
"""

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools.analysis_tool import analizar_negocio, visualizar_datos


def crear_agente(
    model_name: str = "llama-3.3-70b-versatile",
    temperature: float = 0.0,
):
    """
    Strategic business agent with automatic executive insights.
    """

    load_dotenv()

    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        max_tokens=2048,
    )

    system_prompt = """
                Eres un analista senior experto en negocios, ventas y análisis financiero.

                COMPORTAMIENTO GENERAL:
                - Decide automáticamente qué herramienta usar.
                - NUNCA preguntes qué herramienta utilizar.
                - Usa herramientas solo si la pregunta requiere análisis real de datos.
                - Si el usuario pide un gráfico o visualización, usa automáticamente 'visualizar_datos'.
                - No expliques tu razonamiento interno.
                - No menciones qué herramienta utilizaste.
                - Responde de forma clara, ejecutiva y profesional.

                MODO ESTRATÉGICO INTELIGENTE:

                Cuando la respuesta se base en análisis de datos:

                1. Evalúa si existe:
                - Una oportunidad clara de crecimiento
                - Una concentración de riesgo
                - Una caída o tendencia preocupante
                - Un producto con rendimiento atípico
                - Una posibilidad real de optimización

                2. SOLO si detectas algo verdaderamente relevante,
                agrega una sección separada titulada:

                🔎 Insight Estratégico

                3. El insight debe incluir:
                - Observación detectada
                - Impacto potencial
                - Recomendación accionable concreta

                4. Si el análisis no revela nada estratégico relevante,
                NO agregues la sección de Insight.

                Las recomendaciones deben ser:
                - Específicas
                - Aplicables
                - Orientadas a mejorar ingresos, márgenes o eficiencia

                Nunca fuerces un insight si no hay valor real.
                """

    agent = create_agent(
        model=llm,
        tools=[analizar_negocio, visualizar_datos],
        system_prompt=system_prompt,
    )

    return agent