def evaluate_expression(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operator(operands, operator):
        b = operands.pop()
        a = operands.pop()
        if operator == '+':
            operands.append(a + b)
        elif operator == '-':
            operands.append(a - b)
        elif operator == '*':
            operands.append(a * b)
        elif operator == '/':
            operands.append(a / b)

    def to_postfix(expression):
        output = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                output.append(float(num))
                continue
            elif expression[i] == '(':
                operators.append(expression[i])
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            elif expression[i] in '+-*/':
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(expression[i])):
                    output.append(operators.pop())
                operators.append(expression[i])
            i += 1
        while operators:
            output.append(operators.pop())
        return output

    def evaluate_postfix(postfix):
        operands = []
        for token in postfix:
            if isinstance(token, float):
                operands.append(token)
            else:
                apply_operator(operands, token)
        return operands[0]

    postfix = to_postfix(expression)
    return evaluate_postfix(postfix)


print("Zadejte matematický výraz k vyhodnocení (např. 20+(4+3*2)/5):")
user_input = input("Váš výraz: ").replace(" ", "")
try:
    result = evaluate_expression(user_input)
    print(f"Výsledek výrazu '{user_input}' je: {result}")
except Exception as e:
    print(f"Chyba při vyhodnocování výrazu: {e}")
