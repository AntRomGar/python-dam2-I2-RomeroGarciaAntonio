import tkinter as tk  # Importa la librería tkinter para crear interfaces gráficas
from tkinter import messagebox  # Importa messagebox para mostrar mensajes de error o información

# Función que realiza la operación según lo que el usuario seleccionó
def calcular():
    try:
        # Obtiene los valores de las entradas y los convierte a float (números decimales)
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Obtiene la operación seleccionada en el menú desplegable
        operacion = operacion_var.get()

        # Dependiendo de la operación elegida, realiza el cálculo
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            # Evita dividir entre 0
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre 0")
                return
            resultado = num1 / num2
        else:
            # Si no se seleccionó ninguna operación válida
            messagebox.showerror("Error", "Selecciona una operación")
            return

        # Muestra el resultado en la etiqueta de la ventana
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        # Si los valores ingresados no son números
        messagebox.showerror("Error", "Ingresa números válidos")

# Ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora Simple")  # Título de la ventana

# Creación de la entrada del primer número
tk.Label(root, text="Número 1:").grid(row=0, column=0)  # Etiqueta
entry_num1 = tk.Entry(root)  # Caja de texto
entry_num1.grid(row=0, column=1)  # Posicionamiento en la ventana

# Creación de la entrada del segundo número
tk.Label(root, text="Número 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Variable que guardará la operación seleccionada
operacion_var = tk.StringVar(value="Sumar")  # Por defecto "Sumar"

# Menú desplegable para seleccionar operación
tk.Label(root, text="Operación:").grid(row=2, column=0)
tk.OptionMenu(root, operacion_var, "Sumar", "Restar", "Multiplicar", "Dividir").grid(row=2, column=1)

# Botón para calcular el resultado
tk.Button(root, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2)

# Etiqueta donde se mostrará el resultado
label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2)

# Mantiene la ventana abierta
root.mainloop()
