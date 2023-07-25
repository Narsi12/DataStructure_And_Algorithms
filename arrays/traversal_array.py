import array
arr1 = array.array('i',[1,3,4,5,6])

def traversal(array):
    for i in array: #-----------------------> O(n)
        print(i)    #-----------------------> O(1)
traversal(arr1)

# Time complexity is O(n)
# Space complexity is O(1)