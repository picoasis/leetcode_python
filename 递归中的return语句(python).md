

# LEETCODE #231     2的幂

## 题目描述

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 解法1：递归

**一句话解题**：循环除以2，能除到最后结果为1的

**复杂度分析**：时间复杂度O(logn)，空间复杂度O(log n)

**代码**：

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if  n == 0:
            return  False
        elif n == 1:
            return True
        elif n%2 == 0:
            #  ❎① self.isPowerofTwo( n//2 )
            #  ✅② return self.isPowerOfTwo( n//2 )
            return self.isPowerOfTwo( n//2 )     
        else:
            return False
```

**Python语法:  return语句**

函数中如果没有return语句，Python默认返回一个none对象。



![python迭代中的return语句1](递归函数的return语句(python).assets/python迭代中的return语句1.jpg)

## 解法2：用while 代替递归

**一句话解题**: 乘法代替除法

**复杂度分析**：时间复杂度O(logn)，空间复杂度O(1)

**代码**：

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        copy = 2
        while copy < n:
            copy = copy * 2
        return copy == n
```

## 解法3：位运算

**一句话解题：**

1. 满足条件的整数n，因为n=2^x,  x是自然数（0，1，2，3），所以其二进制表示，一定是首位是1 其余位是0。

2. 那么如何表示n呢？

   - 可以通过和n-1的计算关系，n-1一定是首位为0 其余位为1，即 n&(n-1) = 0

   - 并且 n一定大于0

     ![截屏2021-11-23 上午10.57.39](递归函数的return语句(python).assets/截屏2021-11-23 上午10.57.39.png)

   复杂度分析：时间复杂度O(1)空间复杂度O(1)

   **代码：**

   ```
   class Solution:
       def isPowerOfTwo(self, n: int) -> bool:
           if n>0 and n&(n-1)==0:
           	return True
           return False
   ```

   **简化代码**

   ```
   class Solution:
       def isPowerOfTwo(self, n: int) -> bool:
          return n>0 and n&(n-1)==0
   ```

   

