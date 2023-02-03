import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, f"./output")
for filename in os.listdir(path):
    os.remove(os.path.join(path, filename))