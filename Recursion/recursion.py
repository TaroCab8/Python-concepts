"""
find 5! = 5 * 4* 3* 2* 1


"""

def get_recursive_factorial(n):
    if n < 0:
        return -1
    if n < 2: #base case
        return 1
    else:     # recursive call
        return n * get_recursive_factorial(n-1)


def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

print(get_recursive_factorial(6))
print(get_iterative_factorial(6))

"""
trying to reverse a string using recursion

constraints:
- 1 <= s.length <= 10^5
- s[i] os a printable ascii character
"""
#input1
s1 = "hello"
# input2
s2= ["l","a","u","t","a","r","o"]

class Solution:
    def reverse_string(self, s):
        """
        Do not return anything, modify s in-place instead
        """
        if len(s) == 0:
            return s
        else:
            return self.reverse_string(s[1:]) + s[0]
            
       


obj = Solution()

#print(obj.reverse_string(s1))

"""
Fibonacci sequence: 1,1,2,3,5,8,13,21,44,65 etc

Goal: write function to return nth term of Fibonacci Seqience
- fast
- clearly written
- Rock solid

using recursion and memoization
"""
# simple approach not useful for largest numbers

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

    for n in range(1,11):
        print(n, ":",fibonacci(n))


#better approach using memoization
    # 1st version implement explicitly
fibonacci_cache = {}

def fibonacci_other_version(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_other_version(n-1) + fibonacci_other_version(n-2)
    # cache the value and return it
    fibonacci_cache[n] = value
    return value


# for n in range(1,1001):
#     print(n, ":", fibonacci_other_version(n))
    
    





