import sympy

class Parser:
    @staticmethod
    def definition_to_function(s):
        lhs, rhs = s.split("=", 1)
        params = sympy.sympify(lhs).args
        f = sympy.sympify(rhs)
        f_int = sympy.integrate(f, params)
        print(f'The integrated function is {f_int}')

        def func(*arguments):
            argdict = dict(zip(params, arguments))
            result = f.subs(argdict)
            return float(result)

        def func_int(*arguments):
            argdict = dict(zip(params, arguments))
            result = f_int.subs(argdict)
            return float(result)

        return func, rhs, func_int, f_int
