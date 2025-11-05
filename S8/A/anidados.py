# ============================================================
# Anidadas.py
# Registro de paquetes que llegan a casa
# Estructura anidada: lista de diccionarios
# Guarda y carga datos desde un archivo de texto (paquetes.txt)
# ============================================================

from datetime import datetime       # Para validar fechas y horas
from collections import Counter     # Para contar paquetes por día

# ---------- SECCIÓN 1: VARIABLES GLOBALES ----------
ARCHIVO = "./S8/A/paquetes.txt"  # Nombre del archivo donde se guardan los datos
paquetes = []             # Lista principal que almacenará todos los registros


# ---------- SECCIÓN 2: FUNCIONES DE ARCHIVO ----------
def cargar_paquetes():
    """
    Carga los paquetes guardados desde el archivo de texto.
    Cada línea del archivo tiene el formato:
    fecha;hora;tienda;entregado_por
    """
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(";")  # Separa por el carácter ';'
                if len(datos) == 4:
                    paquete = {
                        "fecha": datos[0],
                        "hora": datos[1],
                        "tienda": datos[2],
                        "entregado_por": datos[3],
                    }
                    paquetes.append(paquete)
        print(f"📂 {len(paquetes)} paquetes cargados desde {ARCHIVO}.")
    except FileNotFoundError:
        # Si el archivo no existe, lo crearemos al guardar más tarde
        print("⚠️ No se encontró el archivo. Se creará uno nuevo al guardar.")


def guardar_paquetes():
    """
    Guarda todos los registros en el archivo de texto.
    Cada paquete se guarda en una línea separada con ';' entre los campos.
    """
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in paquetes:
            linea = f"{p['fecha']};{p['hora']};{p['tienda']};{p['entregado_por']}\n"
            f.write(linea)
    print(f"💾 {len(paquetes)} paquetes guardados en {ARCHIVO}.")


# ---------- SECCIÓN 3: FUNCIONES PRINCIPALES ----------
def añadir_paquete(fecha, hora, tienda, entregado_por):
    """
    Añade un nuevo paquete a la lista.
    Incluye validación de formato, campos vacíos y duplicados.
    """
    # Validar que la fecha y la hora tengan el formato correcto
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        print("❌ Formato de fecha u hora incorrecto (usa DD-MM-AAAA y HH:MM).")
        return

    # Validar que los campos no estén vacíos
    if not tienda or not entregado_por:
        print("❌ La tienda y el repartidor no pueden estar vacíos.")
        return

    # Comprobar si ya existe un paquete igual (duplicado)
    for p in paquetes:
        if p["fecha"] == fecha and p["hora"] == hora and p["tienda"].lower() == tienda.lower():
            print("⚠️ Ya existe un paquete igual registrado.")
            return

    # Si todo está bien, se añade el nuevo paquete
    nuevo = {"fecha": fecha, "hora": hora, "tienda": tienda, "entregado_por": entregado_por}
    paquetes.append(nuevo)
    print("✅ Paquete añadido correctamente.")


def mostrar_paquetes():
    """
    Muestra todos los paquetes registrados en la lista.
    Si la lista está vacía, informa al usuario.
    """
    if not paquetes:
        print("📦 No hay paquetes registrados.")
    else:
        print("\n📋 Lista de paquetes:")
        for i, p in enumerate(paquetes, start=1):
            print(f"{i}. {p['fecha']} {p['hora']} | {p['tienda']} | Entregado por {p['entregado_por']}")


def buscar_paquete(campo, valor):
    """
    Busca paquetes según un campo (fecha, tienda o entregado_por)
    y muestra los resultados encontrados.
    """
    if campo not in ("fecha", "tienda", "entregado_por"):
        print("❌ Campo no válido. Usa: fecha, tienda o entregado_por.")
        return

    # Buscar los paquetes que coinciden con el valor indicado
    encontrados = [p for p in paquetes if p[campo].lower() == valor.lower()]
    if encontrados:
        print(f"🔍 Se encontraron {len(encontrados)} resultado(s):")
        for p in encontrados:
            print(f"- {p['fecha']} {p['hora']} | {p['tienda']} | {p['entregado_por']}")
    else:
        print("⚠️ No se encontraron coincidencias.")


def calcular_estadisticas():
    """
    Calcula estadísticas simples:
      - Total de paquetes
      - Día con más paquetes
      - Promedio de paquetes por día
    """
    if not paquetes:
        print("⚠️ No hay datos para calcular estadísticas.")
        return

    # Contar cuántos paquetes llegaron cada día
    conteo = Counter([p["fecha"] for p in paquetes])
    total = len(paquetes)
    max_dia = conteo.most_common(1)[0]  # Día con más paquetes

    print("\n📊 ESTADÍSTICAS:")
    print(f"📦 Total de paquetes: {total}")
    print(f"📅 Día con más paquetes: {max_dia[0]} ({max_dia[1]} paquetes)")
    print(f"📈 Promedio de paquetes por día: {round(total / len(conteo), 2)}")


# ---------- SECCIÓN 4: MENÚ PRINCIPAL ----------
def menu():
    """
    Muestra el menú principal del programa y gestiona las opciones.
    Se ejecuta hasta que el usuario elige salir.
    """
    cargar_paquetes()  # Cargar los datos al iniciar el programa

    while True:
        # Mostrar opciones al usuario
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Añadir nuevo paquete")
        print("2. Buscar paquete")
        print("3. Mostrar todos los paquetes")
        print("4. Ver estadísticas")
        print("5. Guardar y salir")
        print("===================================")

        opcion = input("Elige una opción (1-5): ")

        # Ejecutar la opción elegida
        if opcion == "1":
            fecha = input("📅 Fecha (DD-MM-AAAA): ")
            hora = input("🕓 Hora (HH:MM): ")
            tienda = input("🏬 Tienda: ")
            repartidor = input("🚚 Entregado por: ")
            añadir_paquete(fecha, hora, tienda, repartidor)

        elif opcion == "2":
            campo = input("Buscar por (fecha, tienda, entregado_por): ")
            valor = input("Valor a buscar: ")
            buscar_paquete(campo, valor)

        elif opcion == "3":
            mostrar_paquetes()

        elif opcion == "4":
            calcular_estadisticas()

        elif opcion == "5":
            # Guardar los datos antes de salir
            guardar_paquetes()
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida, inténtalo de nuevo.")


# ---------- SECCIÓN 5: PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    menu()
