import os
import tkinter as tk
import tkinter.messagebox as messagebox
import csv

# Función para mostrar la lista de productos
def mostrar_productos():
    productos_listbox.delete(0, tk.END)
    for producto in productos:
            nombre = producto["Nombre"]
            precio = producto["Precio"]
            costo = producto["Costo"]
            productos_listbox.insert(tk.END, f"{nombre}: ${precio:.2f} Costo: {costo:.2f}")
        

# Función para agregar un producto
def agregar_producto():
    try:
        nombre = nombre_entry.get()
        precio = float(precio_entry.get())
        costo = float(costo_entry.get())
        producto = {"Nombre": nombre, "Precio": precio, "Costo": costo}
        productos.append(producto)
        guardar_productos(productos)
        mostrar_productos()
        nombre_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
        costo_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Los datos deben ser numéricos")

# Función para eliminar un producto
def eliminar_producto():
    nombre = productos_listbox.get(tk.ACTIVE).split(":")[0]
    for i, producto in enumerate(productos):
        if producto["Nombre"] == nombre:
            del productos[i]
            break
    guardar_productos(productos)
    mostrar_productos()



# Función para leer la lista de productos desde el archivo

def leer_productos():
    productos = []
    if os.path.exists("productos.csv"):
        with open("productos.csv", "r") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                producto = {"Nombre": fila["Producto"], "Precio": float(fila["Precio"]), "Costo": float(fila["Costo"])}
                productos.append(producto)
    return productos

# Función para guardar la lista de productos en el archivo


def guardar_productos(productos):
    with open("productos.csv", "w", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Producto", "Precio", "Costo"]) # Escribir los encabezados
        for producto in productos:
            nombre = producto["Nombre"]
            precio = producto["Precio"]
            costo = producto["Costo"]
            writer.writerow([nombre, precio, costo]) # Escribir una fila con los datos del producto
    print('Archivo guardado satisfactoriamente')

# Función principal para ejecutar el programa
def Add_item():
    # Inicializar la interfaz gráfica
    global productos_listbox, nombre_entry, precio_entry, total_label, costo_entry, productos
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
    costo_label = tk.Label(ventana, text="Costo:")
    costo_entry = tk.Entry(ventana)
    agregar_boton = tk.Button(ventana, text="Agregar", command=agregar_producto)
    eliminar_boton = tk.Button(ventana, text="Eliminar", command=eliminar_producto)
    total_label = tk.Label(ventana, text="")

    # Colocar los widgets en la interfaz gráfica
    productos_label.grid(row=0, column=0, padx=10, pady=10)
    productos_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
    nombre_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    nombre_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w", columnspan=2)
    precio_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    precio_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W", columnspan=2)
    costo_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    costo_entry.grid(row=4, column=1, padx=10, pady=10, sticky="W", columnspan=2)
    agregar_boton.grid(row=5, column=0, padx=10, pady=10)
    eliminar_boton.grid(row=5, column=1, padx=10, pady=10)
    total_label.grid(row=6, column=0, padx=10, pady=10)

    #Configuración de tamaño
    productos_listbox.configure(width=40, height=10)
    nombre_entry.configure(width=20)
    nombre_label.configure(width=10)
    precio_entry.configure(width=20)
    precio_label.configure(width=10)
    costo_entry.configure(width=20)
    costo_label.configure(width=10)

    # Mostrar la lista de productos y el total de costos
    mostrar_productos()

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

# Iniciar el programa
if __name__ == "__main__":
    Add_item()