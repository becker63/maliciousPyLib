from importlib import import_module
from termcolor import cprint
import os

module = import_module("termcolor")
debug = False

def getModule():
    roots = []
    origin = ""
    # the base module dict is not subscriptable
    for name,val in module.__dict__.items():
        if name == "__spec__":
            if debug == True:
                for name in val.__dict__:
                    cprint(name, "red", end=" ")
                    cprint( val.__dict__[name], "green")
            spec = val.__dict__
            roots = spec["submodule_search_locations"]
            origin = spec["origin"]
    return [roots, origin]

def saveModuleRootFiles(roots):
    filedata = {}
    for root in roots:
        files = os.listdir(root)
        for filename in files:
            path = f"{root}\{filename}"
            if os.path.exists(path):
                if filename != "__pycache__":
                    with open(path, "r") as file:
                        data = file.read()
                        filedata.update({filename: data})
    if debug == True:
        for key, value in filedata.items():
            cprint(key, "red")
            cprint(value, "green")
    return filedata

def injectModule(origin):
    #print(origin)
    return

if __name__ == "__main__":
    [moduleroots, origin] = getModule()
    filedata = saveModuleRootFiles(moduleroots)
    injectModule(origin)