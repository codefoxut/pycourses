from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, kind, text):
        self.type = kind
        self.text = text

    def __repr__(self):
        return f'`{self.text}`'


def lex(params):
    result = []
    i = 0
    while i < len(params):
        if params[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif params[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif params[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif params[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [params[i]]
            for j in range(i+1, len(params)):
                if params[j].isdigit():
                    digits.append(params[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1

    return result


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


def parse(tokens):
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
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            #  process subexpression
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(params):
    # from design.course1.interpreter.parsing import parse
    tokens = lex(params)
    print(' '.join([str(i) for i in tokens]))

    parsed = parse(tokens)
    print(f'{params} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)')