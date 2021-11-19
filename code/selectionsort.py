'''
选择排序法 O(n^2)
对数组中的元素按大小重新排序
'''
# 方案1: 用新数组存
# 1. 选择数组中最小的元素
# 2. 对数组排序
def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index =i
    return  smallest_index
# 对数组排序
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

testArr =[5,3,9,1,-3,10]
print( selectionSort(testArr) )
# [-3, 1, 3, 5, 9, 10]