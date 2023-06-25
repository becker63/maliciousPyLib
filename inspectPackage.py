from termcolor import cprint
from types import FunctionType
import inspect
from pygments import highlight
from pygments.lexers import PythonLexer 
from pygments.formatters import TerminalFormatter
import sys
import types

#print(sys.argv)
from importlib import import_module



def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def pretifyPy(text):
    return highlight(text, PythonLexer(),TerminalFormatter())


#for name,val in module.__dict__.items():
#    print(name,val)

def printModule(module):
    for name, val in module.__dict__.items(): 
        if(callable(val)):
            if(str(type(val)) == "<class 'builtin_function_or_method'>"):
                cprint(f"{name} {val}", "green")
            else:
                cprint(f"{name} {val}", "red")
                #lines = inspect.getsourcefile(val)
                #pretty= pretifyPy(lines)
                #print(pretty)
                print(val, type(val))    

        else:
            cprint(f"{name}", "magenta")
            print(val)
            print("\n\n")

def saveTofile(module):
    original_stdout = sys.stdout
    with open('output.txt', 'w') as f:
        sys.stdout = f
        for name, val in module.__dict__.items(): 
            if(callable(val)):
                if(str(type(val)) == "<class 'builtin_function_or_method'>"):
                    print(f"{name} {val}")
                else:
                    print(f"{name} {val}")
                    lines = inspect.getsourcefile(val)
                    print(lines)
                    print(type(val))

            else:
                print(f"{name}")
                print(val)
                print("\n\n")
    sys.stdout = original_stdout


module = import_module("numpy")

for name,val in module.__dict__.items():
    if name == "__spec__":
        spec = val.__dict__
        for name in spec:
            cprint(name, "red", end=" ")
            cprint(spec[name], "green")

#saveTofile(module)
printModule(module)

if hasattr(module, '__path__') and getattr(module, '__file__', None) is None:
    print("It's a namespace package.")
#print(module)