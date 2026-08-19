class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        num = 0
        s = s.replace(' ', '')

        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-1 * num)
                elif op == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = ch
                num = 0
        return sum(stack)

