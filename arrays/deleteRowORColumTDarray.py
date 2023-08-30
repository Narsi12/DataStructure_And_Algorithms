import numpy as np

twoDarray = np.array([[11,3,44,5],[10,30,40,50],[33,44,55,66],[87,76,56,45]])

print(twoDarray)

print('***********************')

newArray = np.delete(twoDarray,0,axis=0)  # here axis = 0 menas row and 1 menas column, after twoDarry , 0 is consider as index of row or column

print(newArray)