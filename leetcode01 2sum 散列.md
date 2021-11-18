# **DS哈希表——两数之和 LeetCode01**

 参考链接：https://leetcode-cn.com/problems/two-sum/solution/1liang-shu-zhi-he-by-aver58/

来源：力扣（LeetCode）作者：aver58

# 解法1: 暴力遍历

**一句话解题**：遍历相加

**复杂度分析**：时间复杂度O(n2) 空间复杂度O(1)

**代码**：

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       length = len(nums)
       for i in range(length):
           for j in range(i+1,length):
               if nums[i]+nums[j] == target:
                   return [i,j]
```

#  解法2:python切片

**一句话解题**：找target-nums[i] ,  是否也在nums中。

**复杂度分析**：时间复杂度O(n2)

**代码：**

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       length = len(nums)
       for i in range(length):#1次遍历
           if target-nums[i] in nums[i+1:]:#2次遍历
               return [i,nums.index(target-nums[i],i+1)]
```



python 语法：**index函数**

使用方式：`listname.index(要查找的值，起始索引值，终止索引值) `

index() 方法仅返回值的首次出现。

```
#示例：
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32,2,6)
```

# 解法3: 哈希

**一句话解法：** 使用哈希计算的概念

**复杂度分析：时间复杂度O(n) 空间复杂度O(n)**

**代码**：

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dic = {}
       for i,num in enumerate(nums):
           if num in dic:
               return [i,dic[num]]
           else:
                dic[target-num]= i
```

**python 语法：**注意缩进统一使用空格，或者统一使用tab键enumerateenumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出**数据**和**数据下标**，一般用在 for 循环当中。

```
#示例-普通for循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1
    
#示例-enumerate 的for循
seq = ['one', 'two', 'three']
for i,element in enumerate(seq):
    print(i, element)

```



# 数据结构-哈希

## 是什么

哈希是一个函数处理过程，输入：变长数据，输出：定长数据。

**例子：**

数据：张三-123  李四-567  

目的：查找李四的数据

传统方法：一条条数据进行对比，与‘李四’相等的，为数据存放地址，通过此地址获取对应的数据。

哈希： 存储地址 = f(‘李四’)，因此直接根据‘李四’便得到了对应的地址，获取到对应的数据。

优劣势优势：插入，删除，取用，速度很快劣势：查找操作效率低，如最大值，最小值。——需要求助于其他数据结构，比如二叉树查找。

## 碰撞

散列函数，有可能将不同的值映射成相同的值，这种情况称为碰撞。

通过选择合理的散列函数，可以减小碰撞出现的概率。

散列函数的选择，依赖于键的数据类型（整型，字符串型）散列表的数组长度（常见限制：一般选择质数)

## 两种碰撞解决方案

### 开链法

- 把存储列表设置为二维数组，当哈希值相同时，则在第二个维度按顺序存储。

- 存放一个数据，需要两个连续的存储单位，第一个存放key，第二个存放data。 

`table[pos][index]=key,table[pos][index+1]=data`

- 开链法，适合存储数组长度小的，比如1.5倍的待存储数据长度。 

### 线性探测法

- 发生碰撞时，在计算得到的pos处，按顺序向后查找数组中的空位，进行存储。
- 主table数组存储key,  `table[pos]=key`;  同时增加一个数组来存储data, `values[pos]=data`

- 线性探测，适合存储数组长度大的，比如2倍及以上的待存储数据长度。 

 