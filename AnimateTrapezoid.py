import matplotlib.animation as animation
import matplotlib.pyplot as plt
import NumInt

class AnimateTrapezoid(animation.FuncAnimation):
    def __init__(self):
        super().__init__()


    def init():
        ax.set_ylabel("Y = f(X)")
        ax.set_xlabel("X")
        ax.set_xlim(a - interval, b + interval)
        ax.set_xticks(np.array([]))
        line.set_data([], [])
        return line,

    @classmethod
    def animate_trapezoid(cls, i):
        plt.cla()
        area, X, function_results = NumInt.NumInt.trapezoid(func, a, b, i + 1)
        XTrue, funcResTrue = function_true(func, a, b)
        plot_engine(ax, title, XTrue, funcResTrue,
                    X, function_results, X,
                    X[::n // 5 if n // 5 != 0 else 1])


    anim = mpl.animation.FuncAnimation(fig, animate_trapezoid, init_func=init, frames=n - 1, interval=500)