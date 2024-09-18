from struct import Stack


def infix2Postfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfixList.append(top)
                top = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)


print(infix2Postfix("A + B * ( C - D ) + E"))


def postfixEval(postfixExpr):
    opStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token not in "*/+-":
            opStack.push(int(token))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = doMath(token, op1, op2)
            opStack.push(result)
    return opStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


print(postfixEval("7 8 + 3 2 + /"))
