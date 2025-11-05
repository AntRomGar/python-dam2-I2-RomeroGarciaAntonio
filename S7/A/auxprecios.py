"""
Módulo muy simple para analizar listas de precios.
"""

def minimo(precios):
    return min(precios)

def maximo(precios):
    return max(precios)

def promedio(precios):
    return sum(precios) / len(precios)

def variaciones(precios):
    """Devuelve una lista con la diferencia entre precios consecutivos."""
    return [precios[i+1] - precios[i] for i in range(len(precios)-1)]

def mostrar_resumen(precios):
    print("📊 Resumen de precios:")
    print(" - Mínimo:", minimo(precios))
    print(" - Máximo:", maximo(precios))
    print(" - Promedio:", round(promedio(precios), 2))
