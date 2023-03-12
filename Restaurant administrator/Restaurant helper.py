import os
import tkinter as tk

# Función para mostrar la lista de productos
def mostrar_productos():
    productos_listbox.delete(0, tk.END)
    for nombre, precio in productos.items():
        productos_listbox.insert(tk.END, f"{nombre}: ${precio:.2f}")

# Función para agregar un producto
def agregar_producto():
    nombre = nombre_entry.get()
    precio = float(precio_entry.get())
    productos[nombre] = precio
    guardar_productos()
    mostrar_productos()
    nombre_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)

# Función para eliminar un producto
def eliminar_producto():
    nombre = productos_listbox.get(tk.ACTIVE).split(":")[0]
    del productos[nombre]
    guardar_productos()
    mostrar_productos()

# Función para mostrar el total de costos
def mostrar_total():
    total = sum(productos.values())
    total_label.config(text=f"El total de costos es ${total:.2f}")

# Función para leer la lista de productos desde el archivo
def leer_productos():
    productos = {}
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre, precio = linea.strip().split(",")
                productos[nombre] = float(precio)
    return productos

# Función para guardar la lista de productos en el archivo
def guardar_productos():
    with open("productos.txt", "w") as archivo:
        for nombre, precio in productos.items():
            archivo.write(f"{nombre},{precio}\n")

# Función principal para ejecutar el programa
def main():
    # Inicializar la interfaz gráfica
    global productos_listbox, nombre_entry, precio_entry, total_label, productos
    productos = leer_productos()
    ventana = tk.Tk()
    ventana.title("Sistema de administración de costos de restaurante")

    # Crear los widgets de la interfaz gráfica
    productos_listbox = tk.Listbox(ventana)
    productos_label = tk.Label(ventana, text="Lista de productos")
    nombre_label = tk.Label(ventana, text="Nombre:")
    nombre_entry = tk.Entry(ventana)
    precio_label = tk.Label(ventana, text="Precio:")
    precio_entry = tk.Entry(ventana)
    agregar_boton = tk.Button(ventana, text="Agregar", command=agregar_producto)
    eliminar_boton = tk.Button(ventana, text="Eliminar", command=eliminar_producto)
    total_label = tk.Label(ventana, text="")

    # Colocar los widgets en la interfaz gráfica
    productos_label.grid(row=0, column=0, padx=10, pady=10)
    productos_listbox.grid(row=1, column=0, padx=10, pady=10)
    nombre_label.grid(row=2, column=0, padx=10, pady=10)
    nombre_entry.grid(row=2, column=1, padx=10, pady=10)
    precio_label.grid(row=3, column=0, padx=10, pady=10)
    precio_entry.grid(row=3, column=1, padx=10, pady=10)
    agregar_boton.grid(row=4, column=0, padx=10, pady=10)
    eliminar_boton.grid(row=4, column=1, padx=10, pady=10)
    total_label.grid(row=5, column=0, padx=10, pady=10)

    # Mostrar la lista de productos y el total de costos
    mostrar_productos()
    mostrar_total()

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

# Iniciar el programa
if __name__ == "__main__":
    main()