import numpy as np
import sympy


class HelperFunc:
    @classmethod
    def definition_to_function(cls, s):
        lhs, func_str = s.split("=", 1)
        params = sympy.sympify(lhs).args
        f = sympy.sympify(func_str)
        f_int_str = sympy.integrate(f, params)
        print(f'The integrated function is {f_int_str}')

        def func(*arguments):
            argdict = dict(zip(params, arguments))
            result = f.subs(argdict)
            return float(result)

        def func_integrate(*arguments):
            argdict = dict(zip(params, arguments))
            result = f_int_str.subs(argdict)
            return float(result)

        return func, func_str, func_integrate, f_int_str

    @classmethod
    def input_func(cls):
        func, func_str, func_integrate, f_int_str =\
            cls.definition_to_function(
                input("Please enter the formula:"))
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
        x_true = np.linspace(a - interval / 2, b + interval / 2, num=1000)
        func_res_true = np.array([f(x) for x in x_true])
        return x_true, func_res_true
