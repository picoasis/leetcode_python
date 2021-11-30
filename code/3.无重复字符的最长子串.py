#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxLen = 0
        winStart = 0
        winEnd = 0
        while winEnd < len(s):
            if s[winEnd] not in s[winStart:winEnd]:
                maxLen = max(maxLen,winEnd-winStart+1)
                winEnd = winEnd+1
            else:
                winStart = winStart+s[winStart:winEnd].index(s[winEnd])+1
                winEnd = winEnd+1
        return maxLen

                

# @lc code=end

