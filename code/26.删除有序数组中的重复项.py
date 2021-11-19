#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        lens = len(nums)
        for i in range(1,lens):
            if nums[i] !=  nums[i-1]:
                nums[pos] = nums[i]
                pos += 1
        del nums[pos:lens]
        return len(nums)
# @lc code=end

