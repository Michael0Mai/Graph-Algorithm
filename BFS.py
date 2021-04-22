#coding=utf8

#====================建立树=====================
    
class Node:#定好节点的属性
    def __init__(self, name = None, parent = None):
        self.distance = 0 #和源节点的距离
        self.name = name
        self.children = []
        self.parent = parent         
    
class BFS_Tree():     
    def __init__(self):
        self.root = None   # 应该有一个根节点
    
    def build(self, matrix, start_point):
        count = [] #记录已经搜索过的节点的名字
        temp = []  #已经搜索过,但未加入树的节点
        
        self.root = Node(name = start_point) #处理源节点
        temp.append(self.root)
        count.append(start_point)
        
        while len(count) < len(matrix): #判断节点是否都加入到树中
            for i in range(len(matrix)): #已经搜索当前的节点的邻接点
                if matrix[temp[0].name][i] > 0 and i not in count: 
                    count.append(i) #将搜索过的节点的名字加入到集合中
                    node = Node(name = i) #做成树的节点
                    temp.append(node)  #加入到临时队列中
                    node.parent = temp[0]  #将已经处理好的节点加入到树中
                    temp[0].children.append(node) #将为路径中上一个节点的子节点
                    node.distance = temp[0].distance + matrix[temp[0].name][i] #记录和源节点的距离
            del temp[0]
                
    def _pre_order_list(self, node):#先序遍历,递归查找
        print("源节点到目标节点 %d 的距离是 %d ." %(node.name, node.distance))
        if len(node.children) > 0:
            for child in node.children:
                self._pre_order_list(child)
                
                

                
#============================测试========================  

matrix = [
        [0, 3, 0, 8, 0, 0, 0, 0, 0, 0],
        [1, 0, 9, 4, 0, 6, 0, 0, 0, 0],
        [0, 5, 0, 0, 7, 5, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 0, 0, 9],
        [0, 3, 4, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 1, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 1, 0, 0, 1],
        [0, 0, 0, 0, 4, 2, 0, 0, 4, 0]
        ]
tree = BFS_Tree()

start = 0
print("源节点是: %d ." %start)
tree.build(matrix, start)
tree._pre_order_list(tree.root)