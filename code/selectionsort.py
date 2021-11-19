# '''
# 选择排序法 O(n^2)
# 对数组中的元素按大小重新排序
# '''
# # 方案1: 用新数组存
# # 1. 选择数组中最小的元素
# # 2. 对数组排序
# # 时间复杂度 O(n^2)  空间复杂度 O(n)【查找最小index时，创建中间值】+ （new arr 额外的内存开销）
# def findsmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index =i
#     return  smallest_index
# # 对数组排序
# def selectionSort(arr):
#     newArr=[]
#     for i in range(len(arr)):
#         smallest = findsmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr

# testArr =[5,3,9,1,-3,10]
# print( selectionSort(testArr) )
# # [-3, 1, 3, 5, 9, 10]

# 方案2:不新建arr，当发现更小的元素时，直接交换元素顺序
# 时间复杂度：两次遍历 O(n^2); 空间复杂度：交换时创建中转变量O(n)
def selectionsort(arr):
    for i in range(0,len(arr)):
        # 内循环的 start_index 在变化
        for j in range(i+1,len(arr)):
            # 比较 外循环指定元素 和 内循环遍历元素
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                # print(arr)
    return arr
# test
nums = [4, 1, 5, 10, -1, 9, 3, 2, 13, 7]
t = selectionsort(nums)
print(t)

# 冒泡排序 
# 相对于选择排序， 时间复杂度相同，
# - 稳定性高一些（相邻的同等大小的元素，不会进行重排），
# - 但交换操作数会高于选择排序

def bubulesort(arr):
    for i in range(0,len(arr)):
        # 内循环的 end_index 在变化
        for j in range(0,len(arr)-i-1):
            # 比较相邻元素
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # print(arr)
    return arr
# test

tb = bubulesort(nums)
print(tb)