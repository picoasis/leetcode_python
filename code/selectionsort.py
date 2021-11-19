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

# 方案2:不新建arr，直接交换元素顺序
# 时间复杂度：两次遍历 O(n^2); 空间复杂度：交换时创建中转变量O(n)
nums = [4, 1, 5, 10, -1, 9, 3, 2, 13, 7]
 
count = len(nums)   # count等于nums的长
for i in range(count-1):
    min = i
    for j in range(i+1, count):  # 将剩下的进行遍历，遍历到count
        if nums[min] > nums[j]:
            min = j
    t = 0
    if min != i:    # 若最小值不等于i，进行交换
        nums[i],nums[min] = nums[min],nums[i]
        # t = nums[i]
        # nums[i] = nums[min]
        # nums[min] = t
print(nums)