import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# --- Archivo de almacenamiento ---
ARCHIVO = "S6/diccionarios/tienda_de_discos.txt"

# --- Datos de la tienda de discos ---
cds = []
clientes = []

# --- Guardar y cargar datos ---
def guardar_datos():
    datos = {"cds": cds, "clientes": clientes}
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

def cargar_datos():
    global cds, clientes
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            cds = datos.get("cds", [])
            clientes = datos.get("clientes", [])
        # Asegurar compatibilidad con versiones anteriores (añadir campo 'alquilado_por')
        for cd in cds:
            if "alquilado_por" not in cd:
                cd["alquilado_por"] = None

# --- Funciones principales ---

def agregar_cd():
    titulo = simpledialog.askstring("Nuevo CD", "Título del CD:")
    if titulo:
        cds.append({"titulo": titulo, "disponible": True, "alquilado_por": None})
        actualizar_lista_cds()
        guardar_datos()

def eliminar_cd():
    seleccion = lista_cds.curselection()
    if seleccion:
        indice = seleccion[0]
        del cds[indice]
        actualizar_lista_cds()
        guardar_datos()

def modificar_cd():
    seleccion = lista_cds.curselection()
    if seleccion:
        indice = seleccion[0]
        nuevo_titulo = simpledialog.askstring("Modificar CD", "Nuevo título:")
        if nuevo_titulo:
            cds[indice]["titulo"] = nuevo_titulo
            actualizar_lista_cds()
            guardar_datos()

def cambiar_disponibilidad():
    seleccion = lista_cds.curselection()
    if seleccion:
        indice = seleccion[0]
        cds[indice]["disponible"] = not cds[indice]["disponible"]
        # Si vuelve a estar disponible, limpiamos el campo de alquiler
        if cds[indice]["disponible"]:
            cds[indice]["alquilado_por"] = None
        actualizar_lista_cds()
        guardar_datos()

def agregar_cliente():
    nombre = simpledialog.askstring("Nuevo Cliente", "Nombre del cliente:")
    if nombre:
        clientes.append({"nombre": nombre, "alquileres": 0})
        actualizar_lista_clientes()
        guardar_datos()

def eliminar_cliente():
    seleccion = lista_clientes.curselection()
    if seleccion:
        indice = seleccion[0]
        del clientes[indice]
        actualizar_lista_clientes()
        guardar_datos()

def modificar_cliente():
    seleccion = lista_clientes.curselection()
    if seleccion:
        indice = seleccion[0]
        nuevo_nombre = simpledialog.askstring("Modificar Cliente", "Nuevo nombre:")
        if nuevo_nombre:
            clientes[indice]["nombre"] = nuevo_nombre
            actualizar_lista_clientes()
            guardar_datos()

def registrar_alquiler():
    if not cds or not clientes:
        messagebox.showwarning("Error", "Debe haber al menos un CD y un cliente.")
        return
    seleccion_cd = lista_cds.curselection()
    seleccion_cliente = lista_clientes.curselection()
    if not seleccion_cd or not seleccion_cliente:
        messagebox.showwarning("Error", "Seleccione un CD y un cliente.")
        return
    cd = cds[seleccion_cd[0]]
    cliente = clientes[seleccion_cliente[0]]
    if not cd["disponible"]:
        messagebox.showinfo("Ocupado", "Ese CD no está disponible.")
        return
    # Registrar alquiler
    cd["disponible"] = False
    cd["alquilado_por"] = cliente["nombre"]
    cliente["alquileres"] += 1
    actualizar_lista_cds()
    actualizar_lista_clientes()
    guardar_datos()
    messagebox.showinfo("Éxito", f"{cliente['nombre']} alquiló '{cd['titulo']}'")

def devolver_cd():
    seleccion = lista_cds.curselection()
    if not seleccion:
        messagebox.showwarning("Error", "Seleccione un CD para devolver.")
        return
    indice = seleccion[0]
    cd = cds[indice]
    if cd["disponible"]:
        messagebox.showinfo("Info", "Ese CD ya está disponible.")
        return
    cd["disponible"] = True
    cd["alquilado_por"] = None
    actualizar_lista_cds()
    guardar_datos()
    messagebox.showinfo("Devolución", f"El CD '{cd['titulo']}' fue devuelto y ahora está disponible.")

def calcular_promedio():
    if not clientes:
        messagebox.showinfo("Promedio", "No hay clientes.")
        return
    total = 0
    # Bucle for para recorrer clientes
    for c in clientes:
        total += c["alquileres"]
    promedio = total / len(clientes)
    messagebox.showinfo("Promedio de alquileres", f"{promedio:.2f} por cliente")

# --- Actualizar interfaces ---
def actualizar_lista_cds():
    lista_cds.delete(0, tk.END)
    for cd in cds:
        if cd["disponible"]:
            estado = "Disponible"
        else:
            estado = f"Alquilado por {cd['alquilado_por']}"
        lista_cds.insert(tk.END, f"{cd['titulo']} - {estado}")

def actualizar_lista_clientes():
    lista_clientes.delete(0, tk.END)
    for c in clientes:
        lista_clientes.insert(tk.END, f"{c['nombre']} - Alquileres: {c['alquileres']}")

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("Gestión de la tienda de discos")

# --- CDs ---
frame_cds = tk.Frame(ventana)
frame_cds.pack(side=tk.LEFT, padx=10, pady=10)
tk.Label(frame_cds, text="CDs").pack()
lista_cds = tk.Listbox(frame_cds, width=40, exportselection=False)
lista_cds.pack()
tk.Button(frame_cds, text="Agregar CD", command=agregar_cd).pack(fill="x")
tk.Button(frame_cds, text="Modificar CD", command=modificar_cd).pack(fill="x")
tk.Button(frame_cds, text="Eliminar CD", command=eliminar_cd).pack(fill="x")
tk.Button(frame_cds, text="Cambiar Disponibilidad", command=cambiar_disponibilidad).pack(fill="x")
tk.Button(frame_cds, text="Devolver CD", command=devolver_cd).pack(fill="x")

# --- Clientes ---
frame_clientes = tk.Frame(ventana)
frame_clientes.pack(side=tk.RIGHT, padx=10, pady=10)
tk.Label(frame_clientes, text="Clientes").pack()
lista_clientes = tk.Listbox(frame_clientes, width=40, exportselection=False)
lista_clientes.pack()
tk.Button(frame_clientes, text="Agregar Cliente", command=agregar_cliente).pack(fill="x")
tk.Button(frame_clientes, text="Modificar Cliente", command=modificar_cliente).pack(fill="x")
tk.Button(frame_clientes, text="Eliminar Cliente", command=eliminar_cliente).pack(fill="x")
tk.Button(frame_clientes, text="Registrar Alquiler", command=registrar_alquiler).pack(fill="x")
tk.Button(frame_clientes, text="Calcular Promedio", command=calcular_promedio).pack(fill="x")

# --- Cargar datos al iniciar ---
cargar_datos()
actualizar_lista_cds()
actualizar_lista_clientes()

ventana.mainloop()
