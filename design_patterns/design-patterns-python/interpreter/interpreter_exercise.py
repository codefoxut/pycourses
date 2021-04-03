from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        VARIABLE = auto()

    def __init__(self, kind, text):
        self.type = kind
        self.text = text

    def __repr__(self):
        return '`%s`' % self.text


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    @staticmethod
    def lex(params):
        result = []
        i = 0
        while i < len(params):
            if params[i] == '+':
                result.append(Token(Token.Type.PLUS, '+'))
            elif params[i] == '-':
                result.append(Token(Token.Type.MINUS, '-'))
            elif params[i].isalpha():
                variables = [params[i]]
                for j in range(i + 1, len(params)):
                    if params[j].isalpha():
                        variables.append(params[j])
                        i += 1
                    else:
                        result.append(Token(Token.Type.VARIABLE, ''.join(variables)))
                        break
            else:
                digits = [params[i]]
                for j in range(i + 1, len(params)):
                    if params[j].isdigit():
                        digits.append(params[j])
                        i += 1
                    else:
                        result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                        break
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))

            i += 1

        return result

    def parse(self, tokens):
        result = BinaryExpression()
        have_lhs = False
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.type == Token.Type.INTEGER:
                integer = Integer(int(token.text))
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
                    result.left = Integer(result.value)
                    result.right = Integer(0)
            elif token.type == Token.Type.PLUS:
                result.type = BinaryExpression.Type.ADDITION
            elif token.type == Token.Type.MINUS:
                result.type = BinaryExpression.Type.SUBTRACTION
            elif token.type == Token.Type.VARIABLE:
                if len(token.text) > 1:
                    return 0
                if token.text not in self.variables:
                    return 0
                value = int(self.variables[token.text])
                if not have_lhs:
                    result.left = value
                    have_lhs = True
                else:
                    result.right = value
                    result.left = Integer(result.value)
                    result.right = Integer(0)
            i += 1
        return result

    def calculate(self, expression):
        tokens = self.lex(expression)
        print(tokens)
        try:
            parsed = self.parse(tokens)
            value = parsed.value
        except:
            value = 0

        return value


if __name__ == '__main__':
    exp = '1+2+3'
    val = ExpressionProcessor().calculate(exp)
    print(val)
