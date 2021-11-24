#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustvalues=[0]*n
        for  e in  trust:
            # 为每个人设置信任度，被信任则+1，信任别人则-1，只有法官是n-1
            trustvalues[e[0]-1] += -1
            trustvalues[e[1]-1] += 1
        if n-1 in trustvalues:
            return trustvalues.index(n-1)+1
        else:
            return -1 
# @lc code=end

