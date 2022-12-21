"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

"""
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack=[]
    for c in tokens:
        if c not in '+*-/':
            stack.append(int(c))
        else:
            v1,v2 = stack.pop(),stack.pop()
            if c=='*':
                stack.append(v1*v2)
            elif c == '-':
                stack.append(v2-v1)
            elif c=='+':
                stack.append(v1+v2)
            else:
                stack.append(int(v2/v1))

    return stack.pop()

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

"""
Time/Space: O(N)

"""