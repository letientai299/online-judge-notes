# Setup for python 3 when playing with hackerrank
#  Imports {{{ #
from __future__ import print_function
import inspect
import os
import sys
from itertools import *
import builtins

#  }}} Imports #

#  Config {{{ #
INPUT_FILE = "input.txt"
DEBUG = False
PRINT_TO_FILE = True
FILE_NAME = "output.txt"
#  }}} Config #

#  Setup {{{ #
#  Redirect stdin to the input file if it is existed
if os.path.isfile(INPUT_FILE):
    sys.stdin = open(INPUT_FILE)
    DEBUG = True
    pass

# Prepare the file to write
out = None
if PRINT_TO_FILE:
    out = open(FILE_NAME, "w")
    pass


def print(*args, **kwargs):
    """Overload builtin print to print to file also, if the config is turn on
    """

    if PRINT_TO_FILE:
        builtins.print(*args, **kwargs, file=out)
        pass

        builtins.print(*args, **kwargs)
    pass


def log(*args):
    """Print debugging statement if running locally
    """
    if DEBUG:
        call_line = inspect.stack()[1][4][0].strip()
        assert call_line.strip().startswith("log(")
        call_line = call_line[len("log("):][:-1]
        print("[DEBUG]: %s = %s" % (call_line, *args))
        pass
    pass

def reads():
    return input().split()
    pass


def read_ints():
    return list(map(int, reads()))
    pass
#  }}} Setup #

# Solution code go after this line
