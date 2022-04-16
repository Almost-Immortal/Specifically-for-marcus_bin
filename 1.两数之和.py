
# [1] 两数之和
#

# @lc code=start

# 解法一【慢】
def twoSum(nums, target):
    length = len(nums)
    j=-1
    for i in range(1, length):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = nums.index(target - nums[i])
            break
    if j > 0:
        return [j,i]

# 解法二 【hashmap】
def twoSum2(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i,j]

 twoSum([2,7,11,15], 9)
 
# @lc code=end