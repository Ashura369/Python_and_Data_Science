
nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(len(nums-1)):
            if (nums[i] + nums[j]) == target:
                return nums[i], nums[j]
        

print(twoSum(nums, target))


