arr = [2,5,1,3,4,7]

def shuffle(nums, n):
    return [ i for j in zip(nums[:n],nums[n:]) for i in j]

print(shuffle(arr, 3))