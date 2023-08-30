import numpy as np

twoDarray = np.array([[11,3,44,5],[10,30,40,50],[33,44,55,66],[87,76,56,45]])

print(twoDarray)

#elements insert in cloum axis = 1 menas coulm 0 means row
newTwoDarray = np.insert(twoDarray, 0, [1,2,3,4], axis=0)
print(newTwoDarray)

def accessElements(array, rowIndex, columIndex):
    if rowIndex >= len(array) and columIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][columIndex],"************")
accessElements(twoDarray,1,1)