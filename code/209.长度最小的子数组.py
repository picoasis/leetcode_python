#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0 or len(nums) == 0:
            return 0
        # 滑动窗口
        minLen = len(nums)+1
        winStart = 0
        winEnd = 0
        sums = 0
        while winEnd <len(nums):
            sums += nums[winEnd]
            while sums >= target:
                minLen = min(minLen,winEnd-winStart+1)
                sums = sums - nums[winStart]
                winStart =winStart + 1
            winEnd = winEnd +1
        if minLen>len(nums):
            return 0
        else:
            return minLen

        # 二分查找，前缀和
        # n = len(nums)
        # # 计算前缀和
        # prefix =  [0]*(n+1)
        # for i in range(0,n):
        #     prefix[i+1] = prefix[i]+nums[i]
        # # 定义二分查找
        # def binarySearch(nums,start,target):
        #     left = start +1
        #     right = len(nums)-1
        #     while  left<right:
        #         middle =(left + right) // 2
        #         if nums[middle]-nums[start]>=target:
        #             right =middle
        #         else:
        #             left = middle +1
        #     if nums[left] -nums[start]>=target:
        #         return left -start  
        #     else: return n+1
        # # 寻找满足条件长度最小的子数组
        # minLength = n+1

        # for  i in range(n):
        #     length = binarySearch(prefix,i,target)
        #     minLength = min(minLength,length)
        # if minLength != n+1:
        #     return minLength
        # else:
        #     return 0

        
                
                


# @lc code=end

