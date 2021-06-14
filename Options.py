import sys

from AnimateSimpson import AnimateSimpson
from AnimateTrapezoid import AnimateTrapezoid
from HelperFunc import HelperFunc
from NumInt import NumInt
from Plotting import Plotting


class Const:
    first_level_string = "The options are:\n1. Dynamic Plot (animated)" \
                         "\n2. Static Plot\n3. Exit"
    dynamic_option_string = "You have chosen dynamic plotting.\n" \
                            "The options are:\n1. Trapezoid\n2. Simpson\n3. Back"
    static_option_string = "You have chosen static plotting.\n" \
                           "The options are:\n1. Riemann Left\n2. Riemann Mid\n" \
                           "3. Riemann Right\n4. Trapezoid\n5. Simpson\n6. Back"


def get_menu_choice(s):
    while True:
        try:
            print(s)
            number = int(input("Please choose an option by inputting a number:"))
        except ValueError:
            print("Input is not a number, please try again.")
        else:
            break
    return number


def first_level_options():
    while True:
        number = get_menu_choice(Const.first_level_string)
        if not (number in range(1, 4)):
            print("Number is out of range. Please input 1 to 3.")
        elif number == 1:
            option_dynamic()
        elif number == 2:
            option_static()
        else:
            print("Thank you for using our software.\nExiting program.")
            sys.exit()


def option_dynamic():
    while True:
        number = get_menu_choice(Const.dynamic_option_string)
        if number not in range(1, 4):
            print("number is not in range of 1-3, please try again.")
        elif number == 1:
            anim = AnimateTrapezoid()
        elif number == 2:
            anim = AnimateSimpson()
        else:
            print("Going back one option level.")
            first_level_options()


def option_static():
    while True:
        number = get_menu_choice(Const.static_option_string)
        if not (number in range(1, 7)):
            print("Wrong input, please input a number from 1 to 5.")
        elif number == 1:
            # Left Riemann Sum static plot
            HelperFunc.results(
                *Plotting.static_plot_riemann(
                    NumInt.riemann_left, "Left Riemann Sum", alignment="edge"))

        elif number == 2:
            # Midpoint Riemann Sum static plot
            HelperFunc.results(
                *Plotting.static_plot_riemann(
                    NumInt.riemann_mid, "Midpoint Riemann Sum"))

        elif number == 3:
            # Right Riemann Sum static plot
            HelperFunc.results(
                *Plotting.static_plot_riemann(
                    NumInt.riemann_right, "Right Riemann Sum", -1, 'edge'))

        elif number == 4:
            # Trapezoidal Sum static plot
            HelperFunc.results(
                *Plotting.static_plot(
                    NumInt.trapezoid, "Trapezoidal Sum"))

        elif number == 5:
            # Simpson Sum static plot
            HelperFunc.results(
                *Plotting.static_plot(
                    NumInt.simpson, "Simpson Sum", 10))
        else:
            print("Going back one option level.")
            first_level_options()

