import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapping = {
            "+" : op.add,
            "-" : op.sub,
            "*" : op.mul,
            "/" : op.truediv
        } 
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                result = int(mapping[token](a, b))
                stack.append(result)

        return stack.pop()