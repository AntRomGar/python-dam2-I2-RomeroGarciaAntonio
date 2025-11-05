"""
Programa principal: precios.py
Usa el módulo auxprecios.py para analizar una lista de precios.
"""

import auxprecios as ap

def main():
    print("=== Análisis de Precios ===")
    
    # Lista de ejemplo (puedes cambiarla o pedirla al usuario)
    precios = [10.5, 11.2, 10.8, 12.0, 11.5, 12.3, 12.0]
    
    print("\nLista de precios:", precios)
    
    # Mostrar resumen
    print()
    ap.mostrar_resumen(precios)
    
    # Mostrar variaciones
    print("\n📈 Variaciones entre días:")
    print(ap.variaciones(precios))

if __name__ == "__main__":
    main()
