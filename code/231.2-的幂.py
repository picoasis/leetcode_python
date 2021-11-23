#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 解法1 位运算
        return n>0 and n&(n-1)==0
        # 解法2 迭代
        '''
        if n==0:
            return False
        elif n==1:
            return True
        elif n%2 ==0:
            return self.isPowerOfTwo(n//2)
        else:
            return False
        '''

        # 解法3 用乘法代替除法，while代替迭代
        '''
        if n== 1:
            return True
        copy =2
        while copy < n:
            copy = copy*2
        return copy == n
        '''



# @lc code=end

