import datetime

# ------------------------------
# Función 1: registrar fichaje
# ------------------------------
def registrar_fichaje(nombre, tipo, registros):
    """
    Registra una entrada o salida si no hay un fichaje del mismo tipo
    en las últimas 12 horas.
    Parámetros:
        nombre (str): nombre del empleado
        tipo (str): 'entrada' o 'salida'
        registros (list): lista donde se almacenan los fichajes
    Retorna:
        str: mensaje de confirmación o advertencia
    """
    ahora = datetime.datetime.now()

    # Buscar el último fichaje del mismo tipo para ese empleado
    for reg in reversed(registros):
        if reg["nombre"].lower() == nombre.lower() and reg["tipo"] == tipo:
            hora_ultimo = datetime.datetime.strptime(reg["hora"], "%d/%m/%Y %H:%M:%S")
            diferencia = ahora - hora_ultimo

            # Si han pasado menos de 12 horas, no se permite
            if diferencia.total_seconds() < 12 * 3600:
                return f"⚠️ No puedes registrar otra {tipo} hasta que pasen 12 horas del último fichaje ({hora_ultimo.strftime('%d/%m/%Y %H:%M:%S')})."
            break

    hora_actual = ahora.strftime("%d/%m/%Y %H:%M:%S")
    registro = {"nombre": nombre, "tipo": tipo, "hora": hora_actual}
    registros.append(registro)
    return f"✅ Fichaje de {tipo} registrado para {nombre} a las {hora_actual}"


# ------------------------------
# Función 2: mostrar registros
# ------------------------------
def mostrar_registros(registros):
    """
    Muestra todos los fichajes guardados.
    Parámetros:
        registros (list): lista con los diccionarios de fichajes
    Retorna:
        None
    """
    if not registros:
        print("📭 No hay registros todavía.")
        return

    print("\n=== REGISTROS DE FICHAJES ===")
    for i, reg in enumerate(registros, start=1):
        print(f"{i}. {reg['nombre']} - {reg['tipo']} - {reg['hora']}")
    print("==============================\n")


# ------------------------------
# Función 3: eliminar un registro
# ------------------------------
def eliminar_registro(registros):
    """
    Permite eliminar un registro según su número de lista.
    Controla errores de índice y entradas inválidas.
    Parámetros:
        registros (list): lista con los diccionarios de fichajes
    Retorna:
        None
    """
    if not registros:
        print("📭 No hay registros para eliminar.")
        return

    mostrar_registros(registros)

    try:
        indice = int(input("Introduce el número del registro a eliminar: "))
        if indice < 1 or indice > len(registros):
            raise IndexError
        eliminado = registros.pop(indice - 1)
        print(f"🗑️ Registro eliminado: {eliminado['nombre']} - {eliminado['tipo']} - {eliminado['hora']}")
    except ValueError:
        print("❌ Debes introducir un número válido.")
    except IndexError:
        print("❌ No existe un registro con ese número.")


# ------------------------------
# Función 4: seleccionar opción
# ------------------------------
def pedir_opcion():
    """
    Pide al usuario una opción del menú y la devuelve como número entero.
    Controla errores si la entrada no es válida.
    Retorna:
        int: número de opción seleccionado por el usuario
    """
    try:
        opcion = int(input("Elige una opción (1-4): "))
        if opcion not in (1, 2, 3, 4):
            raise ValueError
        return opcion
    except ValueError:
        print("❌ Opción inválida. Introduce 1, 2, 3 o 4.")
        return None


# ------------------------------
# Programa principal
# ------------------------------
def main():
    """
    Programa principal que gestiona el menú de fichajes:
    1. Registrar entrada/salida
    2. Mostrar registros
    3. Eliminar registro
    4. Salir
    """
    registros = []

    while True:
        print("\n--- MENÚ REGISTRO DE FICHAJES ---")
        print("1. Registrar entrada/salida")
        print("2. Mostrar registros")
        print("3. Eliminar registro")
        print("4. Salir")

        opcion = pedir_opcion()
        if opcion is None:
            continue

        if opcion == 1:
            nombre = input("Nombre del empleado: ").strip()
            tipo = input("¿Entrada o salida?: ").lower().strip()

            if tipo not in ("entrada", "salida"):
                print("❌ Tipo no válido. Debe ser 'entrada' o 'salida'.")
                continue

            mensaje = registrar_fichaje(nombre, tipo, registros)
            print(mensaje)

        elif opcion == 2:
            mostrar_registros(registros)

        elif opcion == 3:
            eliminar_registro(registros)

        elif opcion == 4:
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break


# ------------------------------
# Ejecución del programa
# ------------------------------
if __name__ == "__main__":
    main()
