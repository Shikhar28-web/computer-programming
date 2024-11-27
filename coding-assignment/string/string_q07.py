# Write a function to evaluate a basic calculator expression.


def evaluate_expression(expression):
    def helper(s, index):
        stack = []
        num = 0
        sign = 1

        while index < len(s):
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                stack.append(sign * num)
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                num, index = helper(s, index + 1)
            elif char == ")":
                stack.append(sign * num)
                return sum(stack), index

            index += 1

        stack.append(sign * num)
        return sum(stack), index

    return helper(expression, 0)[0]


print(evaluate_expression("3+(2-1)")) 
