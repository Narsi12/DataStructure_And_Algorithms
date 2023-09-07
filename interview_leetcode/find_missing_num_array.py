mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def findMissing(list,n):
    sum1 = int(n * (n + 1) / 2)
    sum2 = sum(list)
    print(sum1-sum2)
findMissing(mylist,100)


    
def find_missing_numbers(arr):
    if not arr:
        return []

    max_num = max(arr)
    
    all_numbers = set(range(1, max_num + 1))
    
    input_set = set(arr)
    
    missing_numbers = list(all_numbers - input_set)
    
    return missing_numbers

 
missing_nums = find_missing_numbers(mylist)
print("Missing numbers:", missing_nums)
