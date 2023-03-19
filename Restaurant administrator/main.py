import resources
import tkinter as tk
import tkinter.messagebox as messagebox
import csv

cuadro_principal = tk.Tk()
cuadro_principal.title("Sistema de administración de costos de restaurante")

# Configurando el tamaño de la ventana
cuadro_principal.geometry("900x700")

# Leemos productos y los mostramos
productos = resources.leer_productos()

# Crear los widgets de la interfaz gráfica
productos_listbox = tk.Listbox(cuadro_principal)
admin_product = tk.Button(cuadro_principal, text="Administrar productos", command = resources.Add_item)
actualizar = tk.Button(cuadro_principal, text="Actualizar", command = lambda: resources.mostrar_productos(resources.leer_productos(),productos_listbox))

# Acomodamos widgets
productos_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
admin_product.grid(row=2, column=0, padx=10, pady=10)
actualizar.grid(row=2, column=1, padx=10, pady=10)

#Configuración de tamaño
productos_listbox.configure(width=40, height=10)

resources.mostrar_productos(productos,productos_listbox)

cuadro_principal.mainloop()
