n = 4
s = {1,3,5}

def num_ways(n):
    if n == 0 or n == 1:
        return 1
    return num_ways(n-2) + num_ways(n-1)

# print(num_ways(n))

def num_ways_bottom_up(n):
    if n == 0 or n == 1: return 1
    nums = [1,1]
    for i in range(2,n+1):
        nums.append(nums[i-1]+nums[i-2])
    return nums[n]

# print(num_ways_bottom_up(n))

def num_ways_X(n):
    if n == 0: return 1
    total = 0
    for i in {1,2}:
        if n-i >= 0:
            total += num_ways_X(n-i)
    return total

# print(num_ways_X(n))

def num_ways_bottom_up_X(n,x):
    if n == 0: return 1
    nums = [1]
    for i in range(1,n+1):
        total = 0
        for j in x:
            if i - j >= 0:
                total += nums[i-j]
        nums.append(total)
    return nums[n]

# print(num_ways_bottom_up_X(n,{1,2}))

######################################

total = 3
numbers = [1,2,4,10]

def dp(arr,total,i,mem):
    key = str(total)+":"+str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = dp(arr,total,i-1,mem)
    else:
        to_return = dp(arr,total-arr[i],i-1,mem) + dp(arr,total,i-1,mem) 
    mem[key] = to_return
    return to_return

def count_sets_dp(arr,total):
    mem = {}
    return dp(arr,total,len(arr)-1,mem)

print(count_sets_dp(numbers,total))

######################################

