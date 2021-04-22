#coding=utf8
#最小生成树
#prim用在有向图, 不知道可不可以, 从过程看是可以的

import random

class Node:#定好节点的属性
    def __init__(self, name = None, parent = None):
        self.neighbor = []
        self.name = name
        self.children = []
        self.parent = parent
        self.distance = 0 #节点到父节点的距离
        self.edge_count = 0 #节点与树外部连接的边数量

class Prim_Tree():     
    def __init__(self):
        self.root = None   # 应该有一个根节点
        self.distance_sum = 0 #图的最小路径
    
    def build(self, matrix):
        in_tree = []
        
        #计算源节点的数据,将源节点加入树中作为根节点
        nodes = self.build_nodes(matrix) #将节点放到一个数列中
        self.root = nodes[random.randint(0, len(matrix)-1)] #随机抽一个节点作为源节点
        in_tree.append(self.root.name) #记录已经加入到树中的节点
                
        while len(in_tree) < len(matrix):
            temp = [None, None]
            mini_edge = float('inf')
            for i in in_tree: #找到树中连接外部节点的最短边
                if nodes[i].edge_count > 0: # 如果节点还有边与外部连接, 加上这个参数主要是提高效率, 如果节点没有边和外部连接就不用扫描了
                    for j in nodes[i].neighbor:
                        if matrix[i][j] < mini_edge and j not in in_tree:
                            mini_edge = matrix[i][j]
                            temp[0] = i
                            temp[1] = j
            #通过最短边连接的外部节点加入到树中
            in_tree.append(temp[1]) 
            nodes[temp[1]].edge_count = nodes[temp[1]].edge_count - 1 #节点与树外部连接的边数量减少一条
            nodes[temp[1]].parent =  nodes[temp[0]]
            nodes[temp[1]].distance = mini_edge
            nodes[temp[0]].children.append(nodes[temp[1]])
            
            self.distance_sum = self.distance_sum + mini_edge #更新图的最小路径
                        
    def build_nodes(self, matrix):
        nodes = [] #可以看出是一个森林
        for i in range (len(matrix)): #读每个节点的数据
            node = Node(name=i, parent=None)
            nodes.append(node)
            for j in range (len(matrix)):
                if matrix[i][j] > 0:  #读每个节点的邻近节点
                    node.neighbor.append(j) #记录邻接点的距离
                    node.edge_count = node.edge_count + 1 #节点与树外部连接的边数量
        return nodes           
        
    def _pre_order_list(self, node):#先序遍历,递归查找
        if node != self.root:
            print("节点 %d 到父节点 %d 的距离是 %d ." %(node.name, node.parent.name, node.distance))
        else:
            print("根节点是 %d." %(node.name))
        if len(node.children) > 0:
            for child in node.children:
                self._pre_order_list(child)



                
#============================测试========================  
def test():
    matrix = [
            [0, 3, 0, 8, 0, 0, 0, 0, 0, 0],
            [1, 0, 9, 4, 0, 6, 0, 0, 0, 0],
            [0, 5, 0, 0, 7, 1, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 3, 0, 0, 5, 0, 0, 0, 9],
            [0, 3, 1, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 8, 1, 0],
            [0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 1, 0, 0, 1],
            [0, 0, 0, 0, 4, 2, 0, 0, 4, 0]
            ]
    
    
    tree = Prim_Tree()
    tree.build(matrix)
    
    tree._pre_order_list(tree.root)
    print('图的最小路径 %d' %(tree.distance_sum))


test()
