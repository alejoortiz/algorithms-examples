
a = [2,4,1,6,5,40,-1]
b = 20

def search_multipliers(arr,total):
    multipliers = []
    for i in arr:
        if total % i == 0:
            multiple = total/i
            if multiple in arr:
                if multiple < i:
                    numbers = {multiple,i}
                else:
                    numbers = {i,multiple}
                if numbers not in multipliers:
                    multipliers.append(numbers)
    return multipliers

print(search_multipliers(a,b))


arr = [1,2,3,1,2,1,1,5]

def most_frequent(arr):
    frecuency = {}
    for i in arr:
        if i in frecuency.keys():
            frecuency[i] += 1
        else:
            frecuency[i] = 1
    return frecuency

print(most_frequent(arr))

arr = [1,2,3,1,2,1,1,5]

def most_frequent(arr):
    frecuency = {}
    for i in arr:
        if i in frecuency.keys():
            frecuency[i] += 1
        else:
            frecuency[i] = 1
    max_value = max(frecuency, key=frecuency.get) 
    return (max_value,frecuency[max_value])

print(most_frequent(arr))

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,5,10,11,12,13]

def common_values(a,b):
    pl1 = 0
    pl2 = 0
    result = []
    while pl1 < len(a) and pl2 < len(b):
        if a[pl1] == b[pl2]:
            result.append(a[pl1])
            pl1 += 1
            pl2 += 1
        elif a[pl1] < b[pl2]:
            pl1 += 1
        elif a[pl1] > b[pl2]:
            pl2 += 1
    return result

print(common_values(a,b))