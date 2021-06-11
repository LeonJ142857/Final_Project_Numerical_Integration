import numpy as np
import Parser
class HelperFunc:
    @staticmethod
    def input_func():
        func, func_str, func_integrate, f_int_str = Parser.Parser.definition_to_function(input("Please enter the formula:"))
        a = int(input("Please enter the lower bound of integration:"))
        b = int(input("Please enter the upper bound of integration:"))
        n = int(input("Please enter the number of intervals / panels that you want:"))
        return func, func_str, func_integrate, f_int_str, a, b, n

    @staticmethod
    def results(area, true_area):
        print(f'the approximate area under the curve is {area}')
        print(f'the true area under the curve is {true_area}')
        print(f'the difference in measurement is {area - true_area}')
        print(f'the relative true error is {abs((true_area - area) / true_area) * 100}%')

    @staticmethod
    def function_true(f, a, b):
        interval = b - a
        XTrue = np.linspace(a - interval / 2, b + interval / 2, num=1000)
        funcResTrue = np.array([f(x) for x in XTrue])
        return XTrue, funcResTrue
