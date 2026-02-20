# 📊 AI Business Intelligence Assistant – Análisis Inteligente de Ventas con IA

![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat\&logo=google\&logoColor=white)

---

## 📌 Descripción

AI Business Intelligence Assistant es una aplicación interactiva desarrollada con Streamlit + LangChain + Google Gemini, diseñada para analizar datasets de ventas utilizando Inteligencia Artificial conversacional.

La aplicación permite subir archivos CSV o Excel y realizar análisis estratégicos mediante lenguaje natural, generando insights accionables en segundos.

El sistema integra:

* 🤖 Un agente conversacional con memoria optimizada

* 📊 Herramientas de análisis automatizado

* 📈 Generación de visualizaciones dinámicas

* 🧠 Resumen automático de conversación para optimización de tokens

Está pensada para:

* Analistas de negocio

* Emprendedores

* Equipos comerciales

* Desarrolladores interesados en AI aplicada a BI

* MVPs SaaS de analítica inteligente

---

## 🚀 Tecnologías utilizadas

- **Lenguaje: Python 3.12+**

- **Framework Web: Streamlit**

- **IA Generativa: Google Gemini API (gemini-2.5-flash)**

- **Orquestación de IA: LangChain**

- **Visualización de datos: Pandas + Matplotlib**

- **Procesamiento de datos: Pandas**

- **Gestión de estado: Streamlit Session State**

- **Arquitectura modular: Separación por agentes, tools y servicios**

- **Manejo de errores: Control de rate limit (429) y fallos de API**

- **Buenas prácticas: Código limpio, arquitectura escalable tipo SaaS**

---

## ⚙️ Funcionalidades

✅ Carga de archivos CSV y Excel  
✅ Vista previa automática del dataset  
✅ Métricas rápidas del dataset cargado  
✅ Chat conversacional con IA  
✅ Análisis automático de productos más rentables  
✅ Generación de gráficos dinámicos mediante tools  
✅ Memoria conversacional con resumen automático  
✅ Optimización de consumo de tokens  
✅ Manejo profesional de errores (API 429)  
✅ Arquitectura modular lista para escalar  

---
## 🧠 Arquitectura del Sistema

1. La aplicación sigue una arquitectura modular:

2. El usuario carga un archivo CSV/Excel

3. El dataset se almacena en DataStore

4. El agente conversacional recibe el contexto

5. LangChain decide si responder directamente o usar una tool

6. Las tools ejecutan análisis o generan visualizaciones

7. La respuesta se devuelve al usuario

8. El sistema resume automáticamente conversaciones largas para reducir consumo de tokens

---

## 📂 Estructura del proyecto

```bash
AI-Business-Assistant/
│
├── agents/
│   └── analysis_agent.py      # Configuración y creación del agente
│
├── tools/
│   └── analysis_tool.py       # Herramientas de análisis y visualización
│
├── services/
│   └── data_store.py          # Almacenamiento central del dataset
│
├── app.py                     # Aplicación principal Streamlit
│
├── requirements.txt
├── .env                       # Variables de entorno (NO versionado)
└── README.md
```

## 🛠️ Instalación y configuración (modo desarrollo)

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/AI-Business-Assistant.git
cd AI-Business-Assistant
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv env
env\Scripts\activate      # Windows
source env/bin/activate   # Linux / Mac
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```bash
GOOGLE_API_KEY=tu_api_key_aqui
GEMINI_MODEL=gemini-2.5-flash
```

### ▶️ Ejecutar la aplicación

```bash
streamlit run app.py
```
Abrí en el navegador:  
```
http://localhost:8501
```
---

## 📊 Ejemplos de uso

Puedes hacer preguntas como:

* ¿Cuál es el producto más rentable?

* Muéstrame un gráfico de ventas por producto

* ¿Qué categoría genera más ingresos?

* Analiza la tendencia de ingresos mensuales

* ¿Qué oportunidades de mejora detectas?

El asistente responderá utilizando el dataset cargado como contexto.

## 🔐 Seguridad

✔️ API Key protegida mediante variables de entorno  
✔️ `.env` excluido del repositorio  
✔️ Sin credenciales hardcodeadas  
✔️ Manejo controlado de errores de IA  
✔️ Buenas prácticas para proyectos productivos

---

##🏗️ Futuras mejoras

* 📄 Exportación automática de reportes en PDF

* 📊 Dashboard inicial con KPIs automáticos

* 💾 Persistencia en base de datos

* 👥 Sistema multiusuario

* 🔐 Autenticación y control de acceso

---

**Julio Solano**  
🔗 GitHub: [https://github.com/solanomillo](https://github.com/solanomillo)  
📧 Email: [solanomillo144@gmail.com](mailto:solanomillo144@gmail.com)

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.
Podés usarlo, modificarlo y compartirlo libremente.
