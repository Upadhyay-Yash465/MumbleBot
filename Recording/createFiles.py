from fileMethod import filemethod
def createfiles(content, path):
    realPath = open(path).read()
    with open(realPath, "w") as f:
        f.write(content)
    new_path = filemethod(realPath)
    with open(path, "w") as f:
        f.write(new_path)
    return new_path

