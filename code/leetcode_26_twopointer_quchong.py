'''
题目描述
输入：[0,1,1,2,3,3,4,4,4,5]
=>[0,1,2,3,4,5]
输出：去重后的数组长度 6
要求：
1/原地去除重复元素，
2/不使用额外的数组空间
3/仅可使用O（1）额外空间
注意：
1/ 输入数组，为整型数组，
2/输入数组 ，已按增序排好顺序
'''


def removeDuplicates(nums):
    pos = 1
    lens = len(nums)
    print(lens)
    # 将range(i,len) 优化为 range(pos,len)?pos改变会重新for循环吗？
    for i in range(1, len(nums)):
        print("i:", i, "nums[i]:", nums[i])
        if nums[i] != nums[i - 1]:
            nums[pos] = nums[i]
            pos += 1
    del nums[pos:lens]
    # print(nums)
    return len(nums)


arr = [0, 0, 1, 1, 2]
y = removeDuplicates(arr)
print(y)
