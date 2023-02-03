"""
Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels. 

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].

-- Python cases --
Input:
solution.solution(15324)
Output:
    15129,169,25,1

-Constraints:

Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.
"""
"""
class version
"""
# class Solution:
#     def __init__(self):
#         self.n = int
#     sol_list = []   
#     def solution(self,n):
#         if  type(n) is not int or n == 0:
#             return "Invalid input type."
#         new_list = list()
#         for elem in range(1,n+1):
#             if elem * elem < n:
#                 new_list.append(elem)     
#             else:
#                 continue
#         major = (max(new_list)) * (max(new_list))     
#         self.sol_list.append(major)
#         new_n = n - major 
#         if new_n <= 1:
#             self.sol_list.append(new_n)
#             print(self.sol_list)
#             self.sol_list.clear()
#         else: 
#             self.solution(new_n)
#         return self.sol_list

# solution = Solution()
# solution.solution(15324)
# solution.solution(12)
# solution.solution(100)


"""
Working version:
"""

 
# sol_list = list()
# def solution(n):
    
#     if  type(n) is not int or n == 0:
#         return "Invalid input type."
#     new_list = list()
#     for elem in range(1,n+1):
#         if elem * elem < n:
#             new_list.append(elem)     
#         else:
#             continue
#     major = (max(new_list)) * (max(new_list))     
#     sol_list.append(major)
#     new_n = n - major 
#     if new_n <= 1:
#         sol_list.append(new_n)
#         print(sol_list)
#         sol_list.clear()
#     else: 
#         solution(new_n)
#     return sol_list

# solution(15324)
# solution(12)
# solution(100)
# solution("uno")
# solution(0)



# sol_list = list()
# def solution(area):
#     # Your code here
#     if  type(area) is not int or area == 0:
#         print("Invalid input type.")
#         return
#     new_list = list()
#     for elem in range(1,area+1):
#         if elem * elem < area:
#             new_list.append(elem)
#         else:
#             continue
#     major = (max(new_list)) * (max(new_list))
#     sol_list.append(major)
#     new_area = area - major
#     if new_area <= 1:
#         sol_list.append(new_area)
#         print(sol_list)
#         sol_list.clear()
#     else:
#         solution(new_area)
#     return(sol_list)




sol_list = list()
def solution(area):
        
    # Your code here
    if  area <= 1:
        if area == 1:
            print(area)
        else:
            print("Invalid input type.")
        return
        
    new_list = list()
    for elem in range(1, int(area) +1):
        if elem * elem < area:
            new_list.append(elem)
        else:
            continue
    major = (max(new_list)) * (max(new_list))
    sol_list.append(major)
    new_area = area - major
    if new_area <= 1:
        sol_list.append(new_area)
        resp = ",".join(str(e) for e in sol_list)
        print(resp)
        sol_list.clear()
    else:
        solution(new_area)
    
    

solution(-1)
solution(12)
solution(15324)
solution(1+2)

solution(13)
solution(-100)
solution(10.2)