arr = [2,5,1,3,4,7]

def shuffle(nums, n):
    res = []
    for i, j in zip(nums[:n],nums[n:]):
        print(res)
        res += [i,j]
    return res

print(shuffle(arr, len(arr)))