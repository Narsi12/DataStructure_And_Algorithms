"""
1. Merge Sort is a devide and conquer algorithm
2. Divide the input array in two halves and we keep halving recusrively 
until they become too small that cant not be broken further
3. Merge halves by sorting them
"""

def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0]*(n1)
    R = [0]*(n2)

    for i in range(0, n1):
        L[i] = customList[l+i]
    
    for j in range(0, n2):
        R[j] = customList[m+1+j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1
"""
TimeComplexity O(NLogN)
SpaceComplexity O(n)
Note : Refer Big O Notaion for T(N/2) and O(NLogN)
"""
def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList

cList = [2,1,7,6,5,3,4,9,8]
res = mergeSort(cList, 0, 8)
print(res)