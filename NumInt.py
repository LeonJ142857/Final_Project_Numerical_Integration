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
