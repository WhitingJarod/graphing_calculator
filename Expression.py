def tryParse(number: str) -> float:
    try:
        return float(number)
    except:
        return None

###############################################################################

class Expression:
    def __call__(self):
        pass

###############################################################################

class Operand(Expression):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __call__(self, variables = {}) -> Expression:
        for (key, value) in variables.items():
            if key == self.value:
                return Operand(value)
        return self
    
    def __add__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1+num2))
        else:
            return Operand(f"{self.value}+{rhs.value}")

    def __sub__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1-num2))
        else:
            return Operand(f"{self.value}-{rhs.value}")

    def __mul__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1*num2))
        else:
            return Operand(f"{self.value}*{rhs.value}")
            
    def __truediv__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1/num2))
        else:
            return Operand(f"{self.value}/{rhs.value}")
            
    def __mod__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1%num2))
        else:
            return Operand(f"{self.value}%{rhs.value}")
    
    def __pow__(self, rhs: Expression) -> Expression:
        num1, num2 = tryParse(self.value), tryParse(rhs.value)
        if num1 != None and num2 != None:
            return Operand(str(num1**num2))
        else:
            return Operand(f"{self.value}^{rhs.value}")

    def __neg__(self) -> Expression:
        num1 = tryParse(self.value)
        if num1 != None:
            return Operand(str(-num1))
        else:
            return Operand(f"-{self.value}")
    
###############################################################################

class UnaryOperator(Expression):
    precedence = 10
    symbol = None
    right_associative = False

    def __init__(self, rhs: Expression):
        self.rhs = rhs

    def __eq__(self, symbol: str) -> bool:
        return self.symbol == symbol

class Negative(UnaryOperator):
    symbol = '-'
    precedence = 10

    def __call__(self, variables = {}) -> Operand:
        return -self.rhs(variables)

###############################################################################

class BinaryOperator(Expression):
    precedence = -1
    symbol = None
    right_associative = True

    def __init__(self, lhs: Expression, rhs: Expression):
        self.lhs = lhs
        self.rhs = rhs
    
    def __eq__(self, symbol: str) -> bool:
        return self.symbol == symbol

class Plus(BinaryOperator):
    precedence = 0
    symbol = '+'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) + self.rhs(variables)

class Minus(BinaryOperator):
    precedence = 0
    symbol = '-'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) - self.rhs(variables)

class Times(BinaryOperator):
    precedence = 1
    symbol = '*'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) * self.rhs(variables)

class Divide(BinaryOperator):
    precedence = 1
    symbol = '/'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) / self.rhs(variables)

class Modulus(BinaryOperator):
    precedence = 1
    symbol = '%'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) % self.rhs(variables)

class Exponent(BinaryOperator):
    right_associative = False
    precedence = 3
    symbol = '^'

    def __call__(self, variables = {}) -> Operand:
        return self.lhs(variables) ** self.rhs(variables)

###############################################################################

class Absolute:
    def __init__(self, value: Expression):
        self.value = value
    
    def __call__(self, variables = {}) -> Operand:
        value = self.value(variables).value
        num = tryParse(value)
        if num != None:
            return Operand(abs(num))
        else:
            return Operand(f"|{value}|")

###############################################################################

UnaryOperators = [
    Negative,
]

BinaryOperators = [
    Plus,
    Minus,
    Times,
    Divide,
    Modulus,
    Exponent
]
