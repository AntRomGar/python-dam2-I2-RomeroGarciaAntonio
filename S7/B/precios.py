"""
Programa principal: precios.py
Usa el módulo auxprecios.py con manejo de errores.
"""

import auxprecios as ap

def main():
    print("=== Análisis de Precios ===")

    try:
        # Permitir ingresar precios manualmente
        entrada = input("Introduce precios separados por comas (ej: 10.5, 11.2, 9.8): ")
        precios = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]

        print("\nLista de precios:", precios)
        print()
        
        ap.mostrar_resumen(precios)
        
        print("\n📈 Variaciones entre días:")
        print(ap.variaciones(precios))
        
    except ValueError as e:
        print("❌ Error:", e)
    except Exception as e:
        print("⚠️ Ocurrió un error inesperado:", e)
    finally:
        print("🧩 Fin del programa — Gracias por usar el analizador de precios.")

if __name__ == "__main__":
    main()
