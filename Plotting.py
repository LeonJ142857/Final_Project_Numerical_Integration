import matplotlib.pyplot as plt
import numpy as np

import HelperFunc


class Plotting:
    @staticmethod
    def plot_engine(ax, title, XTrue, funcResTrue,
                    X, funcResults, Xminor, Xmajor):
        ax.plot(X, funcResults, label="approximation")
        ax.plot(XTrue, funcResTrue, label="true")
        ax.set_title(title)
        ax.set_xlabel("X")
        ax.set_ylabel("Y = f(X)")
        ax.set_xticks(Xmajor)
        ax.set_xticks(Xminor, minor=True)
        ax.grid(which='minor', alpha=0.3)
        ax.grid(which='major', alpha=1.0)
        ax.fill_between(X, funcResults)
        ax.legend()
        plt.show()

    @staticmethod
    def plot_engine_riemann(ax, title, XTrue, funcResTrue, X, funcResults,
                            Xminor, Xmajor, h, alignment='center'):
        ax.bar(X, funcResults, width=h, alpha=0.2,
               align=alignment, label="approximation")
        ax.plot(XTrue, funcResTrue, label="true")
        ax.plot(X, funcResults, "b.", markersize=3)
        plt.legend()
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y = f(X)')
        ax.set_xticks(Xmajor)
        ax.set_xticks(Xminor, minor=True)
        ax.grid(which='minor', alpha=0.3)
        ax.grid(which='major', alpha=1.0)
        plt.show()

    @classmethod
    def static_plot_riemann(cls, riemann, title, m=1, alignment='center'):
        func, func_str, func_integrate, f_int_str, a, b, n = HelperFunc.HelperFunc.input_func()
        area, x, x_pos, y_pos = riemann(func, a, b, n)
        true_area = func_integrate(b) - func_integrate(a)
        x_true, y_true = HelperFunc.HelperFunc.function_true(func, a, b)
        title += ' of f(x) = ' + func_str + f', n = {n}, ' + f'from a = {a} to b = {b}'
        fig = plt.figure(figsize=(12, 5));
        plt.clf()
        ax = fig.add_subplot(1, 1, 1)
        cls.plot_engine_riemann(ax, title, x_true, y_true, x_pos, y_pos, x,
                            x[::n // 5 if n // 5 != 0 else 1], m * (b - a) / n, alignment)
        return area, true_area

    @classmethod
    def static_plot(cls, num_int, title, mult=1):
        func, func_str, func_integrate, f_int_str, a, b, n = HelperFunc.HelperFunc.input_func()
        area, X, function_results = num_int(func, a, b, n)
        XTrue, funcResTrue = HelperFunc.HelperFunc.function_true(func, a, b)
        title += f" of f(x) = {func_str}, n = {n}, from a = {a} to b = {b}"
        fig = plt.figure(figsize=(12, 5));
        fig.clf();
        ax = fig.add_subplot(1, 1, 1)
        XMajor = X[::mult * (n // 5 if n // 5 != 0 else 1)]
        if mult != 1:
            XMajor = np.concatenate((XMajor, np.array([X[-1]])))
        #     plot_engine(ax, title, XTrue, funcResTrue, X, function_results,
        #                 X[::mult], X[::mult*(n//5 if n//5 != 0 else 1)])
        cls.plot_engine(ax, title, XTrue, funcResTrue, X, function_results,
                    X[::mult], XMajor)
        #     np.concatenate((interpolation_X[::10], np.array([interpolation_X[-1]]))
        true_area = func_integrate(b) - func_integrate(a)
        plt.show()
        return area, true_area
