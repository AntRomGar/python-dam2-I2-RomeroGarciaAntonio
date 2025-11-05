"""
Módulo simple con manejo de errores para analizar listas de precios.
"""

def minimo(precios):
    if not precios:
        raise ValueError("La lista de precios está vacía.")
    return min(precios)

def maximo(precios):
    if not precios:
        raise ValueError("La lista de precios está vacía.")
    return max(precios)

def promedio(precios):
    if not precios:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(precios) / len(precios)

def variaciones(precios):
    if len(precios) < 2:
        raise ValueError("Se necesitan al menos dos precios para calcular variaciones.")
    return [precios[i+1] - precios[i] for i in range(len(precios)-1)]

def mostrar_resumen(precios):
    """Muestra un resumen, con manejo de errores."""
    try:
        print("📊 Resumen de precios:")
        print(" - Mínimo:", minimo(precios))
        print(" - Máximo:", maximo(precios))
        print(" - Promedio:", round(promedio(precios), 2))
    except ValueError as e:
        print("❌ Error al calcular el resumen:", e)
    finally:
        print("✔️ Finalizó el intento de generar el resumen.")
