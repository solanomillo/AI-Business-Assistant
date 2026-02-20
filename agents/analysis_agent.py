"""
Agent configuration for AI Business Assistant.
Handles LLM initialization and tool binding.
"""

from typing import Optional

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.analysis_tool import analizar_negocio, visualizar_datos


def crear_agente(
    model_name: str = "gemini-flash-lite-latest",
    temperature: float = 0.0,
) :
    """
    Create and configure the business analysis agent.

    Args:
        model_name (str): Gemini model to use.
        temperature (float): Model randomness (0 = deterministic).

    Returns:
        AgentExecutor: Configured LangChain agent.
    """

    load_dotenv()

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
    )

    system_prompt = (
        "Eres un analista experto en negocios y datos financieros. "
        "Usa las herramientas disponibles para analizar datos cuando sea necesario. "
        "Responde de forma clara, breve y profesional."
        "Si el usuario solicita un gráfico o visualización, usa la herramienta visualizar_datos."
    )

    agent = create_agent(
        model=llm,
        tools=[analizar_negocio, visualizar_datos],
        system_prompt=system_prompt,
    )

    return agent
