#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgevalues=[0]*(len(edges)+1)
        for e in edges:
            edgevalues[e[0]-1] += 1
            edgevalues[e[1]-1] += 1
        return edgevalues.index(len(edges))+1
# @lc code=end

