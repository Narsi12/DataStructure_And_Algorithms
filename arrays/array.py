import array

my_array = array.array('i') #----------------------> O(1)  Because nothing is intilized
print(my_array)
my_array1 = array.array('i',[1,3,4,5]) #------------------> O(n) memory is allocated 
print(my_array1)


import numpy as np
np_array = np.array([],dtype=int) #----------------------> O(1)  Because nothing is intilized
print(np_array)
np_array1 = np.array([1,3,4,5])#------------------> O(n) memory is allocated 
print(np_array1)

# total space complexity is O(n)