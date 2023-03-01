from Stack import Stack
from Expression import *
import re

patterns = [
    (re.compile("^\d+(?:\.\d+)?"), "NUMBER"),
    (re.compile("^\.\d+"), "NUMBER"),
    (re.compile("^[A-Za-z]+"), "VARIABLE"),
    (re.compile("^\+"), Plus),
    (re.compile("^\-"), Minus),
    (re.compile("^\*"), Times),
    (re.compile("^\/"), Divide),
    (re.compile("^\%"), Modulus),
    (re.compile("^\^"), Exponent),
    (re.compile("^\("), "OPEN_PARENTHESES"),
    (re.compile("^\)"), "CLOSE_PARENTHESES"),
    (re.compile("^\|"), Absolute),
    (re.compile("^\s+"), None),
]

def pushToStack(stack: Stack, output: Stack, token):
    while True:
        top = stack.top()
        if not (top in BinaryOperators or top in UnaryOperators)\
                or top.precedence < token.precedence\
                or (not top.right_associative
                and top.precedence == token.precedence):
            stack(token)
            break
        else:
            output(stack())

def parsePostfix(input: str):
    length = len(input)
    pos = 0
    postfix = Stack()
    stack = Stack()
    variables = []
    last_token = None
    absolute_open = False
    while pos < length:
        substring = input[pos:]
        found = False
        for (pattern, token) in patterns:
            mat = pattern.match(substring)
            if mat:
                found = True
                mat = mat.group(0)
                pos += len(mat)

                if not token:
                    continue
                
                if token == "NUMBER":
                    if last_token == "VARIABLE" or last_token == "CLOSE_PARENTHESES" or (last_token == Absolute and not absolute_open):
                        pushToStack(stack, postfix, Exponent)
                    postfix(Operand(mat))
                
                #TODO: Make this all more streamlined instead of a chain of if statements.
                elif token == "VARIABLE":
                    if last_token == "NUMBER":
                        pushToStack(stack, postfix, Times)
                    elif last_token == "CLOSE_PARENTHESES" or (last_token == Absolute and not absolute_open):
                        pushToStack(stack, postfix, Exponent)
                    postfix(Operand(mat))
                    if not mat in variables:
                        variables.append(mat)

                elif token == "OPEN_PARENTHESES":
                    if last_token == "VARIABLE"\
                            or last_token == "NUMBER"\
                            or (last_token == Absolute and not absolute_open)\
                            or last_token == "CLOSE_PARENTHESES":
                        pushToStack(stack, postfix, Times)
                    stack(token)

                elif token == "CLOSE_PARENTHESES":
                    current = stack()
                    while current != "OPEN_PARENTHESES":
                        postfix(current)
                        current = stack()
                        if not current:
                            print("Unmatched token: )")
                            break
                
                elif token == Absolute:
                    if not absolute_open and (last_token == "VARIABLE"
                            or last_token == "NUMBER"
                            or last_token == Absolute
                            or last_token == "CLOSE_PARENTHESES"):
                        pushToStack(stack, postfix, Times)

                    if absolute_open:
                        current = stack()
                        while current != Absolute:
                            postfix(current)
                            current = stack()
                        postfix(Absolute)
                        absolute_open = False
                    else:
                        stack(token)
                        absolute_open = True

                elif token in BinaryOperators:
                    if not last_token or last_token in BinaryOperators\
                            or last_token in UnaryOperators or last_token == "OPEN_PARENTHESES":
                        if token != Minus:
                            found = False
                            break
                        else:
                            pushToStack(stack, postfix, Negative)
                    else:
                        pushToStack(stack, postfix, token)

                last_token = token
                break
        if not found:
            print(f"Unexpected token: {substring[:1]}")
            return Operand("")

    while stack:
        postfix(stack())
    
    if not postfix: return Operand("")

    def recurse():
        current = postfix()
        if current in UnaryOperators or current == Absolute:
            return current(recurse())
        elif current in BinaryOperators:
            rhs = recurse()
            lhs = recurse()
            return current(lhs, rhs)
        else:
            return current
    
    return (recurse(), variables)

def main():
    while True:
        text = input("Enter an expression.\n").strip()
        if text == "quit":
            break
        (result, var_names) = parsePostfix(text)
        variables = {}
        checked = []
        for name in var_names:
            if name in checked: continue
            checked.append(name)
            value = input(f"(Optional) What is the value of {name}? ").strip()
            if value != "":
                variables[name] = value
        print(f"The answer is {result(variables)}\n")

if __name__ == "__main__": main()
