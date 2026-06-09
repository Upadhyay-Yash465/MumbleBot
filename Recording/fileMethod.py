import os

#splits file name into name, number, and extension
def splitter(file):
    base = os.path.basename(file)
    direct = os.path.dirname(file)
    name, ext = base.rsplit(".", 1)
    parts = name.rsplit("_", 1)
    name = parts[0]
    number = parts[1]
    return direct, name, number, "." + ext

def createFile(directory, file, content):
    a = os.listdir(directory)
    g = []
    if len(a) == 0:
        with open(directory + "\\" + file, "w") as f:
            f.write(content)
    else:
        addedFile = splitter(directory + "\\" + file)
        for i in a:
            if i.startswith(addedFile[1] + "_") and i.endswith(".txt"):
                originalFile = splitter(directory + "\\" + i)
                g.append(originalFile[2])
        if g == []:
            with open(directory + "\\" + file, "w") as f:
                f.write(content)
        else:
            highestVal = max(g)
            print(g, highestVal)
            print(addedFile[2])
            with open(directory + "\\" + addedFile[1] + "_" + str(int(highestVal) + 1) + originalFile[3], "w") as f:
                f.write(content)
    return "done"


