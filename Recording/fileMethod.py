from unittest import result

#splits file name into name, number, and extension
def splitter(file):
    base = file.split("/")[-1]
    name, ext = base.rsplit(".", 1)
    parts = name.rsplit("_", 1)
    return parts[0], parts[1], "." + ext
          
# adds 1 to the number in the file name
def adder(n):
    n = int(n)
    result = n + 1
    return result

# takes a file name, splits it, adds 1 to the number, and returns the new file name
def filemethod(file):
    name, number, ext = splitter(file)
    new_number = adder(number)
    new_file = f"{name}_{new_number}{ext}"
    return new_file

