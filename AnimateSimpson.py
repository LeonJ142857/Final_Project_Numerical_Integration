import matplotlib.animation as animation
import matplotlib.pyplot as plt

import HelperFunc
import NumInt
import Plotting


class AnimateSimpson(animation.FuncAnimation):
    def __init__(self, fig=None, ax=None,
                 frames=None, duration=1000, **kwargs):
        if fig is None:
            if ax is None:
                fig, ax = plt.subplots()
            else:
                fig = ax.get_figure()
        else:
            if ax is None:
                ax = fig.gca()

        func, func_str, func_integrate, f_int_str, a, b, n = \
            HelperFunc.HelperFunc.input_func()
        interval = b - a

        if frames is None:
            frames = n

        self.fig = fig
        self.ax = ax
        self.a = a
        self.b = b
        self.n = n
        self.range = interval
        self.func = func
        self.func_str = func_str
        self.func_integrate = func_integrate
        self.f_int_str = f_int_str
        self.title = f"Trapezoidal Sum of f(x) = {func_str}," \
                     f" n = {n}, from a = {a} to b = {b}"

        super().__init__(fig, self.animate_trapezoid, init_func=self.init,
                         frames=frames, interval=duration, **kwargs)
        plt.show()

    def init(self):
        self.ax.set_ylabel("Y = f(X)")
        self.ax.set_xlabel("X")
        self.ax.set_xlim(self.a - self.range, self.b + self.range)

    def animate_trapezoid(self, i):
        plt.cla()
        area, x, function_results = \
            NumInt.NumInt.simpson(
                self.func, self.a, self.b, 2 * (i + 1))
        x_true, func_res_true = \
            HelperFunc.HelperFunc.function_true(
                self.func, self.a, self.b)
        Plotting.Plotting.plot_engine(
            self.ax, self.title, x_true,
            func_res_true, x, function_results, x[::10],
            x[::10 * (i // 5 if i // 5 != 0 else 1)])
    #
    # anim = mpl.animation.FuncAnimation(fig, animate_trapezoid, init_func=init, frames=n - 1, interval=500)