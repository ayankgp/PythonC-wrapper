from wrapper import *
import numpy as np
from types import MethodType, FunctionType
from ctypes import POINTER, c_double
from function import func


class Calculate:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if isinstance(value, FunctionType):
                setattr(self, name, MethodType(value, self))
            else:
                setattr(self, name, value)
        self.result = np.empty(2)
        self.num = np.ascontiguousarray(self.num)

    def create_params(self, params):
        params.numbers = self.num.ctypes.data_as(POINTER(c_double))
        params.N = len(self.num)
        params.scale = self.scale
        params.result = self.result.ctypes.data_as(POINTER(c_double))

    def get_sum(self):
        params = Parameters()
        self.create_params(params)
        CalculateSum(params)


if __name__ == "__main__":

    Data = dict(
        num=[2., 3.],
        scale=2
    )

    ans = Calculate(**Data)
    ans.get_sum()

    print(func(ans.result))
