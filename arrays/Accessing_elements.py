from array import *
arr1 = array('i',[1,3,4,5,6])

def findelement(array,index):
    if index >= len(array):
        print('There is no such index')  #--------->O(1)
    else:
        print(array[index])              #--------->O(1)
array_index = int(input('Enter a index : '))
findelement(arr1,array_index)

# Time complexity is O(1)
# Space complexity is O(1)