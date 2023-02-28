from Expression import *
from postfix import parsePostfix

def main():
    while True:
        text = input("Enter an expression.\n")
        (result, var_names) = parsePostfix(text)
        variables = {}
        for name in var_names:
            if name in variables: continue
            value = input(f"(Optional) What is the value of {name}? ").strip()
            if value != "":
                variables[name] = value
        print(f"The answer is {result(variables)}\n")

if __name__ == "__main__": main()
