import copy
# 用分而治之算法，编写sum函数
def sumFunc(arr):
    a=copy.deepcopy(arr)#使用深拷贝，防止改变arr的原始值
    sums=0
    if len(a)==0:
        return sums
    else:
        sums = a.pop()+ sumFunc(a)
        return sums

a =[1,2,3,4,5,0,-12,3,9,9.4]
print(a)
print('sum:',sum(a))
print('sumFunc:',sumFunc(a))

# 递归函数，计算列表中包含的元素数
def countFunc(lst):
    l=copy.deepcopy(lst)
    countNum=0
    if len(l)==0:
        return countNum
    else:
        l.pop()
        countNum= 1+countFunc(l)
        return countNum
print(a)
print('len',len(a))
print('countFunc',countFunc(a))

# 找出列表中的最大数字
def findMax(lst):
    l=copy.deepcopy(lst)
    if len(l)==1:
        maxNum = l[-1]
        return maxNum
    else:
        maxNum = l.pop()
        y =findMax(l)
        if maxNum < y:
            maxNum = y
        return maxNum

print(a)
print('max',max(a))
print('findmax',findMax(a))
        
# 二分法
# 用递归实现，arr不能变，变的只有left和right
def binary_search(arr,left,right,item):
    if left>right:
        return None
    midIndex = (left+right)//2
    midValue = arr[midIndex]
    if midValue == item:
        return midIndex
    if midValue > item:
        right = midIndex-1
        return binary_search(arr,left,right,item)
    left = midIndex+1
    return binary_search(arr,left,right,item)
b=[1,2,5,7,9,14]
print(binary_search(b,0,5,3))


# 快速排序
def quicksort(arr):
    lens = len(arr)
    #基线条件
    if lens<2:
        return arr
    # 分解成基线条件
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i<pivot]
        greater =[i for i in arr[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

print(quicksort(a))
print(a)


