import tkinter as tk
import resources
import tkinter.messagebox as messagebox

#Inicializamos lista para guardar nombre y cantidad
productos = []

#Funcion para agregar cantidad a memoria
def agregar_cantidad(cantidad,cuadro):
    try:
        nombre = cuadro.get(tk.ACTIVE).split(":")[0]
        producto = {"Nombre": nombre, "Cantidad": cantidad}
        productos.append(producto)
        print(productos)
    except:
        messagebox.showerror("Error", "Los datos deben ser numéricos")


def venta_diaria():



    #Inicializamos objeto de TK
    venta_diaria = tk.Tk()

# Configurando el tamaño de la ventana
    #venta_diaria.geometry("900x700")
    venta_diaria.title("Agregar cantidad")


    #Creamos widgets
    productos_listbox = tk.Listbox(venta_diaria)
    cantidad_label = tk.Label(venta_diaria, text="Cantidad:")
    cantidad_entry = tk.Entry(venta_diaria)
    agregar_button = tk.Button(venta_diaria, text="Agregar", command = lambda: agregar_cantidad(float(cantidad_entry.get()), productos_listbox))

    # Acomodamos widgets
    productos_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
    cantidad_label.grid(row=2, column=0, padx=10, pady=10)
    cantidad_entry.grid(row=2, column=1, padx=10, pady=10)
    agregar_button.grid(row=3, column=1, padx=10, pady=10, sticky="W", columnspan=2)

    #Configuración de tamaño
    productos_listbox.configure(width=40, height=10)

    #Agregamos items a la lista 
    productos = resources.leer_productos()
    resources.mostrar_productos(productos, productos_listbox)

    venta_diaria.mainloop()

if __name__ == "__main__":
    venta_diaria()
