
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