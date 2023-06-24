from termcolor import cprint
from types import FunctionType
import inspect

import colorama
from pygments import highlight
from pygments.lexers import PythonLexer 
from pygments.formatters import TerminalFormatter


def pretifyPy(text):
    return highlight(text, PythonLexer(),TerminalFormatter())


for name, val in colorama.__dict__.items(): 
    if(callable(val)):
        #cprint(f"{name} {val}", "red")
        lines = inspect.getsource(val)
        pretty= pretifyPy(lines)
        #print(pretty)
        print(lines)
#    else:
#        cprint(f"{name} {val}", "magenta")
#        print(val)
#        print("\n\n")
