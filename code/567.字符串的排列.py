#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
# from collections import Counter
import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)==0 or len(s2)==0 or len(s1)>len(s2):
            return False
        # winStart =0
        # winEnd = winStart +len(s1)-1
        # countS1= Counter(s1)
        # curCountS2 ={}
        # while winEnd<len(s2):
        #     curCountS2 = Counter(s2[winStart:winEnd+1])
        #     if curCountS2 == countS1:
        #         return True
        #     else:
        #         winEnd += 1
        #         winStart += 1
        # return False

        countS1 = {k:0 for k in string.ascii_lowercase}
        countS2 = {k:0 for k in string.ascii_lowercase}
        for s in s1:
            countS1[s] += 1 
        for i in range(len(s2)):
            countS2[s2[i]] += 1
            if i>= len(s1):
                countS2[s2[i-len(s1)]] -= 1
            if countS2 == countS1:
                return True
        return False
        




# @lc code=end

