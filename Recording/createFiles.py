from fileMethod import filemethod
def createfiles(content):
    path = open(r"C:\Users\eyash\Projects\Programming\MumbleBot\MumbleBot\Recording\path.txt").read()
    with open(path, "w") as f:
        f.write(content)
    new_path = filemethod(path)
    with open(r"C:\Users\eyash\Projects\Programming\MumbleBot\MumbleBot\Recording\path.txt", "w") as f:
        f.write(new_path)