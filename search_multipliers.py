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
