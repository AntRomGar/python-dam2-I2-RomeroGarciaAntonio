
"""
==============================
Codigo principal
==============================

def programa():
alumnos = []
n = input("cuantos alumnos?")
for i in range(0, int(n)):
nota = int(input("nota:"))
alumnos.append(nota)
media = sum(alumnos)/len(alumnos)
print("media", media)
print("aprobados:")
for i in alumnos:
if i>=5:
print(i)
"""

def pedir_numero_alumnos():
    """Pide al usuario cuántos alumnos hay, asegurando que sea un entero positivo."""
    while True:
        try:
            n = int(input("¿Cuántos alumnos hay? "))
            if n <= 0:
                print("Debe haber al menos un alumno.")
                continue
            return n
        except ValueError:
            print("Por favor, introduce un número entero válido.")


def pedir_notas(n):
    """Solicita las notas de los alumnos, asegurando que estén entre 0 y 10."""
    notas = []
    for i in range(1, n + 1):
        while True:
            try:
                nota = float(input(f"Introduce la nota del alumno {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, introduce un número válido (usa punto para decimales).")
    return notas


def calcular_media(notas):
    """Calcula la media de las notas, controlando el caso de lista vacía."""
    try:
        return sum(notas) / len(notas)
    except ZeroDivisionError:
        return 0


def mostrar_resultados(notas):
    """Muestra la media y los alumnos aprobados."""
    media = calcular_media(notas)
    print(f"\nMedia de la clase: {media:.2f}")

    aprobados = [n for n in notas if n >= 5]
    if aprobados:
        print("Notas aprobadas:")
        for nota in aprobados:
            print(f" - {nota}")
    else:
        print("Ningún alumno ha aprobado.")


def programa():
    """Función principal del programa."""
    print("=== Cálculo de medias de alumnos ===")
    n = pedir_numero_alumnos()
    notas = pedir_notas(n)
    mostrar_resultados(notas)


# Punto de entrada del programa
if __name__ == "__main__":
    programa()


""" Añadido:
            - pedir_numero_alumnos()
            - pedir_notas(n)
            - calcular_media(notas)
            - mostrar_resultados(notas)

            El código original tenía toda la lógica en una sola función.
            Separar el código en funciones hace que sea más fácil de leer, mantener y probar.
            Además, cada función tiene una única responsabilidad, lo que sigue el principio de 
            una "responsabilidad única" de la programación limpia. """