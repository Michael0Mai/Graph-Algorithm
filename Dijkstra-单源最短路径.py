#coding=utf8
#单源最短路径

import random

class Node:#定好节点的属性
    def __init__(self, name = None, parent = None):
        self.distance = float('inf') #和源节点的距离无穷大
        self.neighbor = []
        self.name = name
        self.children = []
        self.parent = parent  
        
class Dijkstra_Tree():
    def __init__(self):
        self.root = None
    
    def matrix_build_nodes(self, matrix): #通过邻接矩阵建立节点集合
        nodes = [] #可以看出是一个森林
        for i in range (len(matrix)): #读每个节点的数据
            node = Node(name=i, parent=None)
            nodes.append(node)
            for j in range (len(matrix)):
                if matrix[i][j] > 0:  #读每个节点的邻近节点
                    node.neighbor.append([j,matrix[i][j]]) #记录邻接点的距离
        return nodes           
    
    def adjList_build_nodes(self, adjList): #通过邻接表建立节点集合
        pass
    
    def build(self, nodes):
        in_tree = []
        
        #计算源节点的数据,将源节点加入树中作为根节点
        self.root = nodes[random.randint(0, len(nodes)-1)] #随便抽一个节点作为源节点
        self.root.distance = 0 #源节点到自己的距离是0
        in_tree.append(self.root.name) #记录已经加入到树中的节点
        
        while len(in_tree) < len(nodes):
            #松弛边并更新父子关系
            for i in nodes[in_tree[-1]].neighbor: #松弛与最后加入的一个节点连接的节点距离
                if nodes[i[0]].distance > nodes[in_tree[-1]].distance + i[1]:
                    nodes[i[0]].distance = nodes[in_tree[-1]].distance + i[1]
                    #如果外部节点通过新加入节点连接,距离会缩短的话,这个外部节点就成为新加入节点的父节点
                    if nodes[i[0]].parent != None: #删除原来的父子关系
                        nodes[i[0]].parent.children.remove(nodes[i[0]])
                    nodes[i[0]].parent = nodes[in_tree[-1]] #新的父子关系
                    nodes[in_tree[-1]].children.append(nodes[i[0]])
            #加入符合要求的节点到树中
            mini_distance = float('inf')            
            for i in in_tree: #找到树中连接外部节点的最短边
                for j in nodes[i].neighbor:
                    if j[0] not in in_tree and nodes[j[0]].distance < mini_distance:
                        mini_distance = nodes[j[0]].distance
                        temp = j[0]
            in_tree.append(temp) #将与这个最短边连接的节点加入到树中
            
            
    def _pre_order_list(self, node):#先序遍历,递归查找
        if node != self.root:
            print("源节点到目标节点 %d 的距离是 %d ,父节点是 %d" %(node.name, node.distance,node.parent.name))
        else:
            print("这是源节点 %d." %node.name)
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
    
    
    tree = Dijkstra_Tree()
    nodes = tree.matrix_build_nodes(matrix)
    tree.build(nodes)
    
    tree._pre_order_list(tree.root)
    

test()
