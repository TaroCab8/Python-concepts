"""
Given an integer n, generate all the valid combinations of n pairs of parentheses

A combination that contains 1 type of parentheses is valid if evvery opening parenthesis has its closing parenthesis, and it doesn't have a closing parenthesis without having an unused opening parenthesis before
"""
# def is_valid(combination):
#     stack = []
#     for par in combination:
#         if par == '(':
#             stack.append.(par)
#         else:
#             if len(stack) == 0:
#                 return False
#             else:
#                 stack.pop()
#     return len(stack) == 0

#Another version, O(n*2^n) time complexity. O(n*2^n) space complexity.

def is_valid(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff +=1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0

def generate(n):
    def rec(n, diff, comb, combs):
        if diff <0:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n-1, diff-1, comb,combs)
            comb.pop()
    combs = []
    rec(2*n,0,[],combs)
    return combs

print(generate(6))