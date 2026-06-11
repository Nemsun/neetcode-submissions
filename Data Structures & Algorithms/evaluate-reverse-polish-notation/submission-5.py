class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = []
        operators = "+-*/"

        for c in tokens:
            if c in operators:
                if c == "+":
                    num_1 = calc.pop()
                    num_2 = calc.pop()
                    calc.append(num_1 + num_2)
                elif c == "-":
                    num_1 = calc.pop()
                    num_2 = calc.pop()
                    calc.append(num_2 - num_1)
                elif c == "*":
                    num_1 = calc.pop()
                    num_2 = calc.pop()
                    calc.append(num_1 * num_2)
                elif c == "/":
                    num_1 = calc.pop()
                    num_2 = calc.pop()
                    print(calc)
                    calc.append(int(num_2 / num_1))
            else:
                calc.append(int(c))
        return calc[0]