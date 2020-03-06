import os
import ctypes
from ctypes import c_int, c_double, POINTER, Structure

__doc__ = """
Python wrapper for add.c
Compile with:
gcc -O3 -shared -o add.so add.c -lm -fPIC
"""

import subprocess
subprocess.run(["gcc", "-O3", "-shared", "-o", "add.so", "add.c", "-lm", "-fPIC"])


class Parameters(Structure):
    """
    Parameters structure ctypes
    """
    _fields_ = [

        ('numbers', POINTER(c_double)),
        ('N', c_int),
        ('scale', c_double),
        ('result', POINTER(c_double)),
    ]


try:
    lib1 = ctypes.cdll.LoadLibrary(os.getcwd() + "/add.so")
except OSError:
    raise NotImplementedError(
        """
        The library is absent. You must compile the C shared library using: gcc -O3 -shared -o add.so add.c -lm -fPIC
        """
    )

lib1.add.argtypes = (
    POINTER(Parameters),  # parameter field_params
)
lib1.add.restype = None


def CalculateSum(params):
    return lib1.add(
        params
    )