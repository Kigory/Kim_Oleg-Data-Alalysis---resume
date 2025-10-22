from decimal import Decimal
expression = input()


def calculate(exp):
    exp = exp.replace(" ", "")
    exp = exp.replace(",", ".")
    i = 0
    exp_list = []

    def calculator(x1, y1, op):
        x1 = Decimal(x1)
        y1 = Decimal(y1)
        if op == "-":
            return x1-y1
        elif op == "+":
            return x1 + y1
        elif op == "*":
            return x1 * y1
        elif op == "/":
            return x1/y1
        elif op == "^":
            return x1**y1

    while i < len(exp):
        if exp[i].isdigit():
            operand = ''
            while i < len(exp) and (exp[i].isdigit() or exp[i] == "."):
                operand += exp[i]
                i += 1
            exp_list.append(operand)
        elif i <= len(exp):
            exp_list.append(exp[i])
            i += 1

    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    operator_stack = []
    operand_stack = []

    for i in exp_list:
        if i[0].isdigit():
            operand_stack.append(i)
        else:
            if i == '(' or len(operator_stack) == 0:
                operator_stack.append(i)
            elif operator_stack[-1] == "(" and i != ")":
                operator_stack.append(i)
            elif i == ")":
                while True:
                    if operator_stack[-1] == "(":
                        operator_stack.pop(-1)
                        break
                    if len(operator_stack) >= 2:
                        y = operand_stack.pop()
                        x = operand_stack.pop()
                        operand_stack.append(calculator(x, y, operator_stack.pop()))
                    else:
                        break
            elif priority[i] > priority[operator_stack[-1]]:
                operator_stack.append(i)
            else:
                if priority[i] <= priority[operator_stack[-1]]:
                    while (len(operator_stack) > 0 and operator_stack[-1] != "("
                           and priority[i] <= priority[operator_stack[-1]]):
                        y = operand_stack.pop()
                        x = operand_stack.pop()
                        operand_stack.append(calculator(x, y, operator_stack.pop()))
                    operator_stack.append(i)
    while len(operator_stack) != 0:
        y = operand_stack.pop()
        x = operand_stack.pop()
        operand_stack.append(calculator(x, y, operator_stack.pop()))
    return print(*operand_stack)


calculate(expression)
