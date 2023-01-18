import csv

def read_csv(path):
    with open(path, "r+") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            dicionario = {key : value for key, value in iterable}
            data.append(dicionario)
    return data


if __name__ == "__main__":
    data = read_csv("C:/project bucle/world_population.csv")
    print(data[8])
