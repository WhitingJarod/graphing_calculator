from postfix import parsePostfix
from graphing import renderFunction

def main():
    print("\n\nWelcome to the function grapher.\n")
    while True:
        print("--------------------------------------------------------------------------------")
        print("\nYou may use the following operations:")
        print("a+b, a-b, a*b, a/b, a%b, a^b, -a, (a+b), |a+b|")
        print("-(x), -|x|, (x)(x), (x)|x|, |x||x|, 3x, x2, 5x2")
        expr = None
        while True:
            text = input("\nEnter a function expression using the variable x. (or 'q' to quit)\n")
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
            text = input("\nEnter the minimum X value to render. (or blank for -10)\n")
            if text.strip() == "":
                min_x = -10
                break
            try:
                min_x = float(text.strip())
                break
            except:
                print("Unable to parse the minimum X value!")
                continue
        max_x = None
        while True:
            text = input("\nEnter the maximum X value to render. (or blank for 10)\n")
            if text.strip() == "":
                max_x = 10
                break
            try:
                max_x = float(text.strip())
                break
            except:
                print("Unable to parse the maximum X value!")
                continue
        renderFunction(expr[0], min_x, max_x, 1920, 1080)


if __name__ == "__main__": main()
