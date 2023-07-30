from array import *
my_array = array('i',[1,3,4,5,6,7])

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(my_array,8))

# time complexity is O(N)
# Space Complexity is O(1)