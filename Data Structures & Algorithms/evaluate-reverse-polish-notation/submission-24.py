import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        prevItems = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a/b)
        }

        if len(tokens) == 1:
            return int(tokens[0])
    #see operator, take two previous thoings and bang them
        for index, item in enumerate(tokens):
            if item in ops:
                value = ops[item](prevItems[-2], prevItems[-1])
                prevItems.pop()
                prevItems.pop()
                prevItems.append(value)
            else:
                prevItems.append(int(item))
        return prevItems[0]
                 



