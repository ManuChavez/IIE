import csv

labels = []
features = []

def getFeatures(reader, labels):
    f = []
    for label in labels:  
        count = 0
        for row in reader:
            if (row[1]== label and row[4] != "profesor" and row[6] == "da_modificarCampo"):
                count += 1
        f.append(count)
    return f

def getLabels(reader):
    l = []
    for row in reader:
        if (row[4] != "profesor"):
            l.append(row[1])

    l = sorted(set(l), key=l.index)
    l.pop(0)
    return l


with open("dump.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    labels = getLabels(reader)

with open("dump.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    features = getFeatures(reader, labels)
    print(len(features))
    print(len(labels))
    for feature in features:
        print(feature)


