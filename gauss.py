# gauss explanation
# sum = 1 + 2 + 3 + 4 + 5 + 6
# sum = 6 + 5 + 4 + 3 + 2 + 1
# 2sum = 7 + 7 + 7 + 7 + 7 + 7
# 2sum = 7 * (6)
# sum = (7*6)/2
# sum = 6 * (6 + 1)/2
# sum = n * (n + 1)/2

arr = [1,6,5,4,2]

def find_missing(array):
    sum_array = sum(arr)
    n = len(array) + 1
    actual_sum = (n * (n +1)/2)
    return actual_sum - sum_array

print(find_missing(arr)) 

