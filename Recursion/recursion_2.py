# Technical note: find out what Python's recursion limi is with a function from the sys module called getrecursionlimit()
from sys import getrecursionlimit
getrecursionlimit()




#Countdown to zero

def countdown(n):
    print(n)
    if n == 0:
        return # terminate recursion
    else:
        countdown(n-1) #recursive call

countdown(2)

# A factorial function
def factorial_simple(n):
    return 1 if n <= 1 else n * factorial_simple(n -1)

print(factorial_simple(5))

# A factorial recursive and prettier version
def factorial(n):
    print(f'factorial() called with n = {n}')
    return_value = 1 if n <= 1 else n * factorial(n-1)
    print(f'factorial ({n}) returns {return_value}')
    return return_value

factorial(5)

# factorial using loop for time comparision

def factorial_iterative(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value

print(factorial_iterative(5))

# a factorial search using reduce imported from functool
from functools import reduce
def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])

print(factorial_reduce(5))


# speed comparison of factorials implementations


# setup_string = """
# print("Recursive:")
# def factorial_simple(n):
#     return 1 if n <= 1 else n * factorial_simple(n - 1)
# """
# from timeit import timeit
# timeit("factorial_simple(5)", setup=setup_string, number=1000000)

# Traverse a Nested List
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

for index, item in enumerate(names): 
    print(index, item)


#the above formula doesn't satisfy the need of counting all "leaf" elements
#instead 
def count_leaf_items(item_list):
    """
    Recursively counts and returns the number of leaf items in a (potentially nested) list
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count

print(count_leaf_items([names]))

# Detect Palindromes with recursion is arguably silly, but it makes an intersting excercise to think recursevily
def is_palindrom(word):
    """ Return true if word is a palindrom, False if not."""
    return word == word[::-1]

print(is_palindrom("foo"))
print(is_palindrom("racecar"))
print(is_palindrom("troglodyte"))
print(is_palindrom("civic"))

# using recursion

def is_palindrom_recursion(word):
    """Return True if word if word is a palindrome, False if not."""
    if len(word) <=1:
        return True
    else: 
        return word[0] == word[-1] and is_palindrom_recursion(word[1:-1])

    #base cases
print(is_palindrom_recursion(""))
print(is_palindrom_recursion("a"))

print(is_palindrom_recursion("foo"))
print(is_palindrom_recursion("racecar"))
print(is_palindrom_recursion("troglodyte"))
print(is_palindrom_recursion("civic"))

# Sort with quiksort: a good example of a problem that very naturally suggest a recursive approach.

"""
Quicksort is a divide-and conquer algorithm. Supose you have a list of objects to sort. You start by choosing an item in the list, calle the pivot item. This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the alorithm are as follows:
- Choose the pivot item.
- Partition the list into two sublists:
    1. Those items that are less than the pivot item
    2. Those items that are greater than the pivot item
- Quicksort the sublists recursively
"""

import statistics

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else: pivot = statistics.median(
        [
            numbers[0],
            numbers[len(numbers) // 2],
            numbers[-1]
        ]
    )
    items_less, pivot_items, items_greater = (
        [n for n in numbers if n < pivot],
        [n for n in numbers if n == pivot],
        [n for n in numbers if n > pivot]
    )

    return (
        quicksort(items_less) +
        pivot_items +
        quicksort(items_greater)
    )

    # base case
print(quicksort([]))
print(quicksort([42]))

    # recursive cases
print(quicksort([5,2,6,3]))
print(quicksort([10,-3,21,6,-8]))