class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPar = ["(", "[", "{"]
        closePar = [")", "]", "}"]
        flips = str.maketrans({
            "[": "]", "]": "[",
            "(": ")", ")": "(",
            "{": "}", "}": "{"
        })
        if len(s) % 2 != 0 or s[0] not in openPar:
            return False
        for char in s:
            if char in openPar:
                stack.append(char)
            elif char in closePar:
                if stack != []:
                    if char == stack[-1].translate(flips):
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True
        else:
            return False