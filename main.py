from postfix import parsePostfix
from graphing import renderFunction
import sys

def graphingMode():
    print("\n--------------------------------------------------------------------------------\n")
    print("Graphing mode")
    print("\nYou may use the following operations:")
    print("a+b, a-b, a*b, a/b, a%b, a^b, -a, (a+b), |a+b|")
    print("-(x), -|x|, (x)(x), (x)|x|, |x||x|, 3x, x2, 5x2")
    while True:
        expr = None
        while True:
            text = input("\nEnter a function expression using the variable x. (or 'q' to quit)\n> ")
            if text.strip() == "q":
                return
            try:
                expr = parsePostfix(text)
                for name in expr[1]:
                    if name != 'x':
                        print(f"Invalid variable: {name}")
                        continue
                float(expr[0]({"x": 1}))
                break
            except:
                print("Unable to parse the expression!")
                continue
        min_x = None
        while True:
            text = input("Enter the minimum X value to render. (or blank for -10) ")
            if text.strip() == "":
                min_x = -10
                break
            try:
                min_x = float(text.strip())
                break
            except:
                print("Unable to parse the minimum X value as a number!")
                continue
        max_x = None
        while True:
            text = input("Enter the maximum X value to render. (or blank for 10) ")
            if text.strip() == "":
                max_x = 10
                break
            try:
                max_x = float(text.strip())
                break
            except:
                print("Unable to parse the maximum X value as a number!")
                continue
        renderFunction(expr[0], min_x, max_x, 1600, 900)

def calculatorMode():
    print("\n--------------------------------------------------------------------------------\n")
    print("Calculator mode")
    print("\nYou may use the following operations:")
    print("a+b, a-b, a*b, a/b, a%b, a^b, -a, (a+b), |a+b|")
    print("-(x), -|x|, (x)(x), (x)|x|, |x||x|, 3x, x2, 5x2")
    while True:
        expr = None
        text = input("\nEnter a function expression using zero or more multi-letter variables. (or 'q' to quit)\n> ")
        if text.strip() == "q":
            return
        try:
            (expr, names) = parsePostfix(text)
            variables = {}
            for name in names:
                while True:
                    text = input(f"(Optional) What is the value of {name}? ").strip()
                    if text == "": break
                    try:
                        number = float(text)
                        variables[name] = number
                        break
                    except:
                        print(f"Unable to parse the input as a number!")
            result = expr(variables)
            print(result)
        except:
            print("Unable to parse equation!")

modes = {
    "g": graphingMode,
    "c": calculatorMode
}

def main():
    print("\n--------------------------------------------------------------------------------\n")
    print("Main menu")
    while True:
        print("\nAvailable options: (g)raphing, (c)alculator, (q)uit")
        text = input("Please enter an option.\n> ").strip()
        if text in modes:
            modes[text]()
            print("\n--------------------------------------------------------------------------------\n")
            print("Main menu")
        elif text == "q":
            sys.exit()
        else:
            print("Not a valid option!")


if __name__ == "__main__": main()
