import tkinter as tk
import resources
import tkinter.messagebox as messagebox
import csv
import os
import datetime

#Inicializamos lista para guardar nombre y cantidad
productos = []
cantidades = []

def leer_cantidad():
    cantidad = []
    if os.path.exists("cantidad.csv"):
        with open("cantidad.csv", "r") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                cantidad = {"Nombre": fila["Producto"], "Precio": float(fila["Precio"]), "Costo": float(fila["Costo"]), "Cantidad": int(fila["Cantidad"])}
                cantidades.append(cantidad)
    return cantidades


def guardar_cantidad(productos,nombre):
    with open(nombre, "w", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Producto", "Precio", "Costo", 'Cantidad']) # Escribir los encabezados
        for producto in productos:
            nombre = producto["Nombre"]
            precio = producto["Precio"]
            costo = producto["Costo"]
            cantidad = producto["Cantidad"]
            writer.writerow([nombre, precio, costo, cantidad]) # Escribir una fila con los datos del producto
    print('Archivo guardado satisfactoriamente')

#Funcion para agregar cantidad a memoria
def agregar_cantidad(cantidad,cuadro,lista):
    try:
        
        productos = resources.leer_productos() # 
        nombre = cuadro.get(tk.ACTIVE).split(":")[0]
        for i, producto in enumerate(productos):
            if producto["Nombre"] == nombre:
                precio = producto["Precio"]
                costo = producto["Costo"]
                lista.insert(tk.END, f"{nombre}: ${precio:.2f}| Costo: {costo:.2f}| Cantidad {cantidad}|")
                cantidad_entry.delete(0, tk.END)
                dict_aux = {"Nombre": nombre, "Precio": precio, "Costo": costo,  "Cantidad": cantidad}
                cantidades.append(dict_aux)
                break
    except:
        messagebox.showerror("Error", "Los datos deben ser numéricos")

def eliminar_producto(lista,cantidad):
    nombre = lista.get(tk.ACTIVE).split(":")[0]
    for i, producto in enumerate(cantidad):
        if producto["Nombre"] == nombre:
            del cantidades[i]
            break
        
    # Eliminar el item seleccionado de la lista
    for index in lista.curselection():
        lista.delete(index)


def venta_diaria():


    #Inicializamos campos entry como variables globales para poder borrar valores al ejecutar funciones
    global cantidad_entry, venta

    #Inicializamos objeto de TK
    venta_diaria = tk.Toplevel()

# Configurando el tamaño de la ventana
    #venta_diaria.geometry("900x700")
    venta_diaria.title("Agregar cantidad")
    venta_diaria.configure(bg="#1E1E1E")

    #Creamos widgets
    productos_listbox = tk.Listbox(venta_diaria,bg="#2B2B2B", fg="white", selectbackground="#0078D7", selectforeground="white", font=("Helvetica", 9))
    cantidad_label = tk.Label(venta_diaria, text="Cantidad:",bg="#1E1E1E", fg="white", font=("Helvetica", 12))
    cantidad_entry = tk.Entry(venta_diaria,bg="#1E1E1E", fg="white", font=("Helvetica", 12))
    agregar_button = tk.Button(venta_diaria, text="Agregar",bg="#0078D7", fg="white", font=("Helvetica", 9), command = lambda: agregar_cantidad(int(cantidad_entry.get()), productos_listbox,venta)if cantidad_entry.get() else messagebox.showerror("Error", "Ingresa un valor valido"))
    guardar_button = tk.Button(venta_diaria, text="Guardar venta",bg="#0078D7", fg="white", font=("Helvetica", 9), command = lambda: guardar_cantidad(cantidades,str(datetime.datetime.now().strftime("%Y-%m-%d") + datetime.datetime.now().strftime(" %H;%M;%S") + '.csv')))
    venta = tk.Listbox(venta_diaria,bg="#2B2B2B", fg="white", selectbackground="#0078D7", selectforeground="white", font=("Helvetica", 12))
    eliminar_venta = tk.Button(venta_diaria, text="Eliminar",bg="#0078D7", fg="white", font=("Helvetica", 9), command= lambda: eliminar_producto(venta,cantidades))
    mi_label = tk.Label(venta_diaria, text="->",bg="#1E1E1E", fg="white")

    # Acomodamos widgets
    productos_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
    cantidad_label.grid(row=2, column=0, padx=10, pady=10)
    cantidad_entry.grid(row=2, column=1, padx=10, pady=10)
    agregar_button.grid(row=3, column=1, padx=10, pady=10, sticky="W", columnspan=2)
    guardar_button.grid(row=2, column=5, padx=10, pady=10, sticky="W")
    venta.grid(row=1, column=5, padx=10, pady=10)
    eliminar_venta.grid(row=2, column=5, padx=10, pady=10, sticky="E")
    mi_label.grid(row=1, column=4, padx=10, pady=10)

    #Configuración de tamaño
    productos_listbox.configure(width=50, height=10)
    venta.configure(width=50, height=10)
    guardar_button.configure(width=20, height=1)
    eliminar_venta.configure(width=20, height=1)

    #Agregamos items a la lista 
    productos = resources.leer_productos()
    resources.mostrar_productos(productos, productos_listbox)

    venta_diaria.mainloop()

if __name__ == "__main__":
    venta_diaria()
