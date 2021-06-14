import numpy as np

class NumInt:
    @staticmethod
    def riemann_left(f, a, b, n):
        if n == 0:
            return
        x = np.linspace(a, b, num=n + 1)
        x_left = x[:-1]
        y_left = np.array([f(c) for c in x_left])
        total = np.sum(y_left) * (b - a) / n
        return total, x, x_left, y_left

    @staticmethod
    def riemann_mid(f, a, b, n):
        if n == 0:
            return
        x = np.linspace(a, b, num=n + 1)
        x_mid = (x[:-1] + x[1:]) / 2
        y_mid = np.array([f(c) for c in x_mid])
        total = np.sum(y_mid) * (b - a) / n
        return total, x, x_mid, y_mid

    @staticmethod
    def riemann_right(f, a, b, n):
        if n == 0:
            return
        x = np.linspace(a, b, num=n + 1)
        x_right = x[1::]
        y_right = np.array([f(c) for c in x_right])
        total = np.sum(y_right) * (b - a) / n
        return total, x, x_right, y_right

    @staticmethod
    def trapezoid(f, a, b, n):
        if n == 0:
            return
        X = np.linspace(a, b, num=n + 1)
        function_results = np.array([f(x) for x in X])
        weights = np.full((n + 1,), 2)
        weights[0] = 1
        weights[-1] = 1
        h = (b - a) / n
        total = np.sum(weights * function_results)
        total *= (b - a) / (2 * n)
        return total, X, function_results

    @classmethod
    def calc_parabola_vertex(cls, x1, y1, x2, y2, x3, y3):
        denom = (x1 - x2) * (x1 - x3) * (x2 - x3);
        A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom;
        B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom;
        C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom;
        return A, B, C

    @classmethod
    def simpson_util(cls, X1, X2, X3, Y1, Y2, Y3):
        interpolation_X = np.array([])
        interpolation_Y = np.array([])
        for x1, x2, x3, y1, y2, y3 in zip(X1, X2, X3, Y1, Y2, Y3):
            A, B, C = cls.calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
            par_func = lambda A, B, C, a: A * (a ** 2) + B * a + C
            int_X = np.linspace(x1, x3, 10)
            int_Y = par_func(A, B, C, int_X)
            interpolation_X = np.concatenate((interpolation_X, int_X))
            interpolation_Y = np.concatenate((interpolation_Y, int_Y))
        return interpolation_X, interpolation_Y


    @classmethod
    def simpson(cls, f, a, b, n):
        X = np.linspace(a, b, num=n + 1)
        Y = np.array([f(x) for x in X])

        X1 = np.array(X[0::2])
        X2 = np.array(X[1::2])
        X3 = np.array(X[2::2])
        Y1 = np.array(Y[0::2])
        Y2 = np.array(Y[1::2])
        Y3 = np.array(Y[2::2])
        interpolation_X, interpolation_Y = cls.simpson_util(X1, X2, X3, Y1, Y2, Y3)

        weights = np.full((n + 1,), 1)
        h = (b - a) / n
        weights[1::2] = 4
        weights[2::2] = 2
        weights[-1] = 1
        total = np.sum(weights * Y)
        total *= h / 3
        return total, interpolation_X, interpolation_Y

