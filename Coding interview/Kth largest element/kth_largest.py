"""
Given an array of integers 'arr' and an integer 'k', find the kth largest element


"""
# 1rst solution: O(kn) time complexity, O(1) space complexity 
def kth_largest(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

alist= [2,5,3,6,12,7,66,8]


print(kth_largest(alist, 6))

# 2nd solution, sorting: O(nlogn) time complexity, 

def kth_largest2(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

print(kth_largest2(alist,6))

# 3rd solution: using priority cue using heaps. O(n+klogn)
import heapq

def kth_largest3(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

print(kth_largest3(alist, 4))