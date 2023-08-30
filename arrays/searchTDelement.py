import numpy as np

twoDarray = np.array([[11,3,44,5],[10,30,40,50],[33,44,55,66],[87,76,56,45]])

print(twoDarray)

def searchTDarray(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return "the element is located at "+str(i)+" "+ str(j)
    return "The element is not found"

print(searchTDarray(twoDarray,55))