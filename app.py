import streamlit as st
import pandas as pd

from agents.analysis_agent import crear_agente
from services.data_store import DataStore


# ======================================
# Configuración de página
# ======================================

st.set_page_config(
    page_title="AI Business Assistant",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<h1 style='margin-bottom:0;'>🧠 AI Business Assistant</h1>
<p style='font-size:18px; color:gray; margin-top:5px;'>
Plataforma inteligente para analizar datos de ventas, detectar oportunidades 
y responder preguntas estratégicas sobre tu negocio usando IA.
</p>
""", unsafe_allow_html=True)

st.divider()

# ======================================
# Sidebar informativa
# ======================================

with st.sidebar:
    st.header("🧠 ¿Qué hace esta aplicación?")
    st.markdown("""
    Este asistente analiza tus datos de ventas y puede ayudarte a:

    - 📈 Detectar el producto más rentable  
    - 📊 Generar visualizaciones dinámicas  
    - 💡 Identificar oportunidades de crecimiento  
    - 🔎 Analizar ingresos, cantidades y tendencias  
    - 🤖 Responder preguntas sobre tu negocio en lenguaje natural  

    ---
    **Modo de uso:**
    1. Sube tu archivo CSV o Excel  
    2. Haz preguntas en el chat  
    3. Obtén análisis automatizados con IA
    """)


# ======================================
# Inicializar estado
# ======================================

if "agente" not in st.session_state:
    st.session_state.agente = crear_agente()

if "df" not in st.session_state:
    st.session_state.df = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "summary" not in st.session_state:
    st.session_state.summary = ""


# ======================================
# Función: Resumir conversación
# ======================================

def resumir_conversacion(messages):
    """
    Resume la conversación para reducir el uso de tokens.
    """

    prompt = (
        "Resume la siguiente conversación en máximo 5 líneas "
        "manteniendo el contexto clave del negocio:\n\n"
    )

    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"

    respuesta = st.session_state.agente.invoke(
        {
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    contenido = respuesta["messages"][-1].content

    if isinstance(contenido, list):
        return "".join(
            bloque.get("text", "")
            for bloque in contenido
            if bloque.get("type") == "text"
        )

    return contenido


# ======================================
# Carga de archivo
# ======================================

st.subheader("📂 Carga de Datos")

uploaded_file = st.file_uploader(
    "Sube tu archivo de ventas (Excel o CSV)",
    type=["xlsx", "csv"],
)


if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state.df = df
        DataStore.df = df

        # Reiniciar memoria al cargar nuevo archivo
        st.session_state.messages = []
        st.session_state.summary = ""

        st.success("Archivo cargado correctamente ✅")
        
        # Métricas rápidas del dataset
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Filas", df.shape[0])

        with col2:
            st.metric("Columnas", df.shape[1])

        with col3:
            st.metric(
                "Columnas Numéricas",
                len(df.select_dtypes(include="number").columns),
            )


        st.subheader("📊 Vista previa")
        st.dataframe(df.head(50), width="stretch")

    except Exception as error:
        st.error(f"Error al cargar el archivo: {error}")


# ======================================
# Chat IA Conversacional
# ======================================
if st.session_state.df is not None:

    st.divider()
    st.subheader("🤖 Asistente de Negocio")

    # Mostrar historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    pregunta = st.chat_input(
        "Escribe tu pregunta sobre el negocio:"
    )

    if pregunta:

        # Guardar mensaje usuario
        st.session_state.messages.append(
            {"role": "user", "content": pregunta}
        )

        with st.chat_message("user"):
            st.markdown(pregunta)

        with st.chat_message("assistant"):
            with st.spinner("Analizando datos..."):

                MAX_MESSAGES_BEFORE_SUMMARY = 12
                KEEP_LAST_MESSAGES = 6

                # 🔥 Solo resumir si realmente es necesario
                if len(st.session_state.messages) > MAX_MESSAGES_BEFORE_SUMMARY:

                    # Solo resumimos los mensajes antiguos
                    mensajes_antiguos = st.session_state.messages[:-KEEP_LAST_MESSAGES]

                    resumen = resumir_conversacion(mensajes_antiguos)

                    st.session_state.summary = resumen

                    # Reemplazamos historial por resumen + últimos mensajes
                    st.session_state.messages = (
                        [{"role": "system", "content": resumen}]
                        + st.session_state.messages[-KEEP_LAST_MESSAGES:]
                    )

                # Enviar conversación actual
                try:
                    respuesta = st.session_state.agente.invoke(
                        {
                            "messages": st.session_state.messages
                        }
                    )

                except Exception as e:

                    error_text = str(e)

                    if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                        texto = (
                            "⚠️ Se alcanzó el límite diario de la API (Free Tier).\n\n"
                            "Por favor espera unos minutos o activa facturación "
                            "en Google AI Studio para continuar usando el asistente."
                        )

                        st.error(texto)

                        # No guardamos como respuesta normal
                        st.stop()

                    else:
                        st.error("❌ Ocurrió un error inesperado.")
                        st.exception(e)
                        st.stop()


                contenido = respuesta["messages"][-1].content

                if isinstance(contenido, list):
                    texto = "".join(
                        bloque.get("text", "")
                        for bloque in contenido
                        if bloque.get("type") == "text"
                    )
                else:
                    texto = contenido

                st.markdown(texto)

        # Guardar respuesta
        st.session_state.messages.append(
            {"role": "assistant", "content": texto}
        )


else:
    st.info("Sube un archivo para comenzar.")
