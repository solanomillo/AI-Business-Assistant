from typing import Dict

import pandas as pd


class BusinessService:
    """Business metrics calculation service."""

    REQUIRED_COLUMNS = {
        "producto",
        "cantidad",
        "precio_venta",
        "costo_unitario",
    }

    @staticmethod
    def calcular_metricas(df: pd.DataFrame) -> Dict:
        """
        Calculate key business metrics from sales data.

        Args:
            df (pd.DataFrame): Sales dataset.

        Returns:
            Dict: Business metrics summary.
        """

        if df.empty:
            return BusinessService._empty_response()

        missing_columns = BusinessService.REQUIRED_COLUMNS - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"Faltan columnas requeridas: {missing_columns}"
            )

        df = df.copy().fillna(0)

        # Calcular métricas básicas
        df["ingreso_total"] = df["cantidad"] * df["precio_venta"]
        df["costo_total"] = df["cantidad"] * df["costo_unitario"]
        df["ganancia"] = df["ingreso_total"] - df["costo_total"]

        ganancia_total = float(df["ganancia"].sum())

        ganancia_por_producto = (
            df.groupby("producto", as_index=True)["ganancia"]
            .sum()
            .sort_values(ascending=False)
        )

        if ganancia_por_producto.empty:
            return BusinessService._empty_response()

        producto_mas_rentable = ganancia_por_producto.idxmax()
        mejor_ganancia = float(ganancia_por_producto.max())

        margen = (
            (df["precio_venta"] - df["costo_unitario"])
            .div(df["precio_venta"].replace(0, 1))
        )

        margen_promedio = float(margen.mean() * 100)

        # ⚡ Limitamos el dict para no enviar demasiados tokens
        top_productos = (
            ganancia_por_producto.head(5).round(2).to_dict()
        )

        return {
            "ganancia_total": round(ganancia_total, 2),
            "ganancia_por_producto": top_productos,
            "producto_mas_rentable": producto_mas_rentable,
            "mejor_ganancia": round(mejor_ganancia, 2),
            "margen_promedio": round(margen_promedio, 2),
        }

    @staticmethod
    def _empty_response() -> Dict:
        """Return safe empty metrics response."""
        return {
            "ganancia_total": 0.0,
            "ganancia_por_producto": {},
            "producto_mas_rentable": "N/A",
            "mejor_ganancia": 0.0,
            "margen_promedio": 0.0,
        }
