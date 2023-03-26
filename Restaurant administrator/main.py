import resources
import tkinter as tk
import ventas


cuadro_principal = tk.Tk()
cuadro_principal.title("Sistema de administración de costos de restaurante")

# Iniciar tema oscuro
cuadro_principal.configure(bg="#1E1E1E")
tk.Label(cuadro_principal, text="Lista de productos", font=("Helvetica", 16), fg="white", bg="#1E1E1E").grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="W")

# Configurando el tamaño de la ventana
cuadro_principal.geometry("900x700")

# Leemos productos y los mostramos
productos = resources.leer_productos()

# Crear los widgets de la interfaz gráfica
productos_listbox = tk.Listbox(cuadro_principal, bg="#2B2B2B", fg="white", selectbackground="#0078D7", selectforeground="white", font=("Helvetica", 12))
admin_product = tk.Button(cuadro_principal, text="Administrar productos", bg="#0078D7", fg="white", font=("Helvetica", 12), command = resources.Add_item)
actualizar = tk.Button(cuadro_principal, text="Actualizar", bg="#0078D7", fg="white", font=("Helvetica", 12), command = lambda: resources.mostrar_productos(resources.leer_productos(),productos_listbox))
venta = tk.Button(cuadro_principal, text="Agregar venta", bg="#0078D7", fg="white", font=("Helvetica", 12), command = ventas.venta_diaria)
ruta = tk.Button(cuadro_principal, text="Agregar ruta", bg="#0078D7", fg="white", font=("Helvetica", 12))

# Acomodamos widgets
productos_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
admin_product.grid(row=2, column=0, padx=10, pady=10, sticky="W")
actualizar.grid(row=2, column=0, padx=10, pady=10, sticky="E", columnspan=2)
venta.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)
ruta.grid(row=4, column=0, padx=10, pady=10, sticky="NSEW", columnspan=2)

#Configuración de tamaño
productos_listbox.configure(width=40, height=10)
venta.configure(width=30, height=1)
actualizar.configure(width=15, height=1)

resources.mostrar_productos(productos,productos_listbox)

cuadro_principal.mainloop()