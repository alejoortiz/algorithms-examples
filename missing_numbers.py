array = [1,6,5,4,2]

def find_missings(array):
    numbers = []
    for i in range(len(array)+1):
        if i not in array:
            numbers.append(i)
    return numbers

print(find_missings(array)) 
