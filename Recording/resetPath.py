from fileMethod import splitter

def resetpath(path):
    with open(path, "r") as f:
        realPath = f.read()
        dir, name, number, ext = splitter(realPath)
    g = int(number)
    g = 0
    with open(path, "w") as f:
            f.write(dir + "\\" + name + "_" + str(g) + ext)
