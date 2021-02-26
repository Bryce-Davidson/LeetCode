arr = [2,5,1,3,4,7]

def shuffle(nums, n):
    new = []

    for i, j in zip(nums[:n],nums[n:]):
         new.extend([i,j])
    return new

print(shuffle(arr, 3))