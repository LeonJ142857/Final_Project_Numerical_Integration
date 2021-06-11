# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import sympy
import matplotlib as mpl
import matplotlib.pyplot as plt
import Parser

if __name__ == '__main__':
    results(*static_plot_riemann(riemann_left, "Left Riemann Sum", alignment="edge"))
    results(*static_plot_riemann(riemann_mid, "Midpoint Riemann Sum"))
    results(*static_plot_riemann(riemann_right, "Right Riemann Sum", -1, 'edge'))
    results(*static_plot(trapezoid, "Trapezoidal Sum"))

    func, func_str, func_integrate, f_int_str, a, b, n = input_func()
    interval = b - a

    title = f"Trapezoidal Sum of f(x) = {func_str}, n = {n}, from a = {a} to b = {b}"

    fig = plt.figure(figsize=(12, 5));
    plt.clf();
    ax = fig.add_subplot(1, 1, 1)
    line, = ax.plot([], [], lw=2)
    x_ticks = ax.get_xticks()


    def init():
        ax.set_ylabel("Y = f(X)")
        ax.set_xlabel("X")
        ax.set_xlim(a - interval, b + interval)
        ax.set_xticks(np.array([]))
        line.set_data([], [])
        return line,


    def animate_trapezoid(i):
        plt.cla()
        area, X, function_results = trapezoid(func, a, b, i + 1)
        XTrue, funcResTrue = function_true(func, a, b)
        plot_engine(ax, title, XTrue, funcResTrue,
                    X, function_results, X,
                    X[::n // 5 if n // 5 != 0 else 1])


    anim = mpl.animation.FuncAnimation(fig, animate_trapezoid, init_func=init, frames=n - 1, interval=500)


    def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
        denom = (x1 - x2) * (x1 - x3) * (x2 - x3);
        A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom;
        B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom;
        C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom;
        return A, B, C


    def simpson_util(X1, X2, X3, Y1, Y2, Y3):
        interpolation_X = np.array([])
        interpolation_Y = np.array([])
        for x1, x2, x3, y1, y2, y3 in zip(X1, X2, X3, Y1, Y2, Y3):
            A, B, C = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
            par_func = lambda A, B, C, a: A * (a ** 2) + B * a + C
            int_X = np.linspace(x1, x3, 10)
            int_Y = par_func(A, B, C, int_X)
            interpolation_X = np.concatenate((interpolation_X, int_X))
            interpolation_Y = np.concatenate((interpolation_Y, int_Y))
        return interpolation_X, interpolation_Y


    def simpson(f, a, b, n):
        X = np.linspace(a, b, num=n + 1)
        Y = np.array([f(x) for x in X])

        X1 = np.array(X[0::2])
        X2 = np.array(X[1::2])
        X3 = np.array(X[2::2])
        Y1 = np.array(Y[0::2])
        Y2 = np.array(Y[1::2])
        Y3 = np.array(Y[2::2])
        interpolation_X, interpolation_Y = simpson_util(X1, X2, X3, Y1, Y2, Y3)

        weights = np.full((n + 1,), 1)
        h = (b - a) / n
        weights[1::2] = 4
        weights[2::2] = 2
        weights[-1] = 1
        total = np.sum(weights * Y)
        total *= h / 3
        return total, interpolation_X, interpolation_Y


    results(*static_plot(simpson, "Simpson Sum", 10))

    func, func_str, func_integrate, f_int_str, a, b, n = input_func()
    interval = b - a
    title = f"Trapezoidal Sum of f(x) = {func_str}, n = {n}, from a = {a} to b = {b}"

    fig = plt.figure(figsize=(12, 5))
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))


    def init():
        ax.set_ylabel("f(X)")
        ax.set_xlabel("X")
        ax.set_xlim(a - interval, b + interval)
        ax.set_ylim(1, -1)
        ax.set_xticks(np.array([]))
        line.set_data([], [])
        return line,


    def animate_simpson(i):
        plt.cla()
        area, X, function_results = simpson(func, a, b, 2 * (i + 1))
        XTrue, funcResTrue = function_true(func, a, b)
        plot_engine(ax, title, XTrue, funcResTrue,
                    X, function_results, X[::10],
                    X[::10 * (i // 5 if i // 5 != 0 else 1)])


    anim = mpl.animation.FuncAnimation(fig, animate_simpson, init_func=init, frames=n, interval=1000)
    


