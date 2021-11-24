# 图  人际关系
graph ={}
graph['You'] =['Bob','Claire','Alice']
graph['Alice']=['Peggy']
graph['peggy']=[]
graph['Bob']=['Anuj']
graph['Anuj']=[]
graph['Claire'] =['Thom','Jonny']
graph['Thom']=[]
graph['Jonny']=[]

# BFS 算法
# s1 创建1个队列，存储要检查的人---s2 从队列中弹出1个人—— s3检查这个人是否是销售商——s4a 是则完成查找，
# s4b 不是则将这个人的邻居加入队列——s5再回到s2

from collections import deque
def person_is_seller(name):
        # 假设以m结尾的名字，是seller
        return name[-1] == 'm'

def bfs_seach(name):
    search_queue = deque()
    search_queue += graph['You']
    searched =[]
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + ' is a mango seller!')
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

bfs_seach('You')