class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == "+":
                left, right = stk.pop(), stk.pop()
                stk.append(left+right)
            elif token == "-":
                left, right = stk.pop(), stk.pop()
                stk.append(right-left)
            elif token == "*":
                left, right = stk.pop(), stk.pop()
                stk.append(left*right)
            elif token == "/":
                left, right = stk.pop(), stk.pop()
                stk.append(int(right/left))
            else:
                stk.append(int(token))

        return stk[-1]
"""
stk = []
if "+":
    left, right = pop both from stack
    add sum to stk
elif "-":
    left, right = pop from stack,
    right - left = diff
    stk.append(diff)
elif "*":
    same as plus
elif "/":
    same as minus
else:
    append to stk


"""