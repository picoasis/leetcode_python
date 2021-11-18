'''
二分查找：
1. 适用顺序列表的查找
2. n个元素中查找1个，次数最多log2（n）
'''
#输入：有序数组1个，指定元素1个
#输出：如果元素在数组中，则返回其位置

def binary_search(mylist,item):
    low = 0
    high = len(mylist)-1

    while low <= high:
        mid = ( low + high ) // 2
        guess = mylist[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return
# 测试
my_list = [1,3,5,7,9]
print( binary_search(my_list,3) )
print( binary_search(my_list,-3) )
