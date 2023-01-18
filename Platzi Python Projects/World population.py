import Lectura_csv
import matplotlib.pyplot as plt

def extrae_columna(dic):
    diccionario = {}
    for element in dic:
        pais = element['Country/Territory']
        dato = element['World Population Percentage']
        diccionario[pais] = float(dato)
    return diccionario

def gen_piechar(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.show()

data = Lectura_csv.read_csv("C:/project bucle/world_population.csv")
diccionario = extrae_columna(data)

keys = list(diccionario.keys())
values = list(diccionario.values())
gen_piechar(keys, values)

