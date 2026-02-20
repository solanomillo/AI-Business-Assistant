from langchain.tools import tool
from services.business_service import BusinessService
from services.data_store import DataStore
import matplotlib.pyplot as plt


@tool
def visualizar_datos(column_x: str, column_y: str) -> str:
    """
    Genera un gráfico de barras usando dos columnas del dataset.
    column_x: columna categórica
    column_y: columna numérica
    """

    df = DataStore.df

    if df is None:
        return "No hay datos cargados para visualizar."

    if column_x not in df.columns or column_y not in df.columns:
        return "Las columnas especificadas no existen en el dataset."

    try:
        resumen = (
            df.groupby(column_x)[column_y]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots()
        resumen.plot(kind="bar", ax=ax)

        ax.set_title(f"{column_y} por {column_x}")
        ax.set_ylabel(column_y)
        ax.set_xlabel(column_x)

        plt.xticks(rotation=45)
        plt.tight_layout()

        path = "grafico_generado.png"
        plt.savefig(path)
        plt.close(fig)

        return f"Gráfico generado correctamente. Archivo guardado como {path}"

    except Exception as e:
        return f"Error al generar el gráfico: {str(e)}"



@tool
def analizar_negocio() -> str:
    """
    Analiza métricas del negocio usando el DataFrame almacenado en memoria.
    """

    df = DataStore.df

    if df is None or df.empty:
        return "No hay datos cargados para analizar."

    metricas = BusinessService.calcular_metricas(df)

    return (
        f"📊 Resumen del negocio:\n"
        f"- Ganancia total: ${metricas['ganancia_total']:,.0f}\n"
        f"- Producto más rentable: {metricas['producto_mas_rentable']}\n"
        f"- Margen promedio: {metricas['margen_promedio']}%\n"
        f"- Top productos: {metricas['ganancia_por_producto']}"
    )
