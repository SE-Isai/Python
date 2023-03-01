import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A","B","C"]
    value = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(value , labels = labels)
    plt.show()
    plt.savefig("pie.png")
    plt.close