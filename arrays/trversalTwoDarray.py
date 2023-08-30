import numpy as np

twoDarray = np.array([[11,3,44,5],[10,30,40,50],[33,44,55,66],[87,76,56,45]])

print(twoDarray)

def traveseTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traveseTDarray(twoDarray)