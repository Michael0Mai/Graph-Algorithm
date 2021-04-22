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

class Bellman_Ford_Tree():
    def __init__(self):
        self.root = None
        self.false = False #是否有负环
    
    def matrix_build_nodes(self, matrix): #通过邻接矩阵建立节点集合
        nodes = [] #可以看出是一个森林
        for i in range (len(matrix)): #读每个节点的数据
            node = Node(name=i, parent=None)
            nodes.append(node)
            for j in range (len(matrix)):
                if matrix[i][j] != 0:  #读每个节点的邻近节点
                    node.neighbor.append([j,matrix[i][j]]) #记录邻接点的距离
        return nodes        
    
    def adjList_build_nodes(self, adjList): #通过邻接表建立节点集合
        pass
    
    def build(self, nodes):
        #计算源节点的数据,将源节点加入树中作为根节点
        self.root = nodes[random.randint(0, len(nodes)-1)] #随便抽一个节点作为源节点
        #self.root = nodes[0]
        self.root.distance = 0 #源节点到自己的距离是0
        
        for i in range(len(nodes)-1):#对每条边做节点数-1次处理
            done = []
            self.relax(nodes, self.root, done) #松弛每一条边
            print("--------")
        
        self.check_loop(nodes)
        
            
            
    def relax(self, nodes, node, done):
        print(node.name)
        #松弛边并更新父子关系
        for i in node.neighbor: #松弛与最后加入的一个节点连接的节点距离
            if nodes[i[0]].distance > node.distance + i[1]:
                nodes[i[0]].distance = node.distance + i[1]
                #如果外部节点通过新加入节点连接,距离会缩短的话,这个外部节点就成为新加入节点的父节点
                if nodes[i[0]].parent != None: #删除原来的父子关系
                    nodes[i[0]].parent.children.remove(nodes[i[0]])
                nodes[i[0]].parent = node #新的父子关系
                node.children.append(nodes[i[0]])
        done.append(node.name)
        #递归检查
        if len(done) < len(nodes):
            for child in node.children:
                if child.name not in done:
                    self.relax(nodes, child, done)
            
    def check_loop(self, nodes): #逐条边检查,看是否有负环
        for i in nodes: #循环每个节点
            for j in i.neighbor: #循环每个节点的每条边
                if nodes[j[0]].distance > i.distance + j[1]:
                    self.false = True
                    return
        
            
            
    def _pre_order_list(self, node):#先序遍历,递归查找
        if self.false == False:
            if node != self.root:
                print("目标节点 %d ,距离 %d ,父节点 %d" %(node.name, node.distance,node.parent.name))
            else:
                print("这是源节点 %d." %node.name)
            if len(node.children) > 0:
                for child in node.children:
                    self._pre_order_list(child)
        else:
            print("存在负环")

                
                
#============================测试========================  
def test():
    A = [
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


    B = [
        [0, -10, 0, -9, 0, 0, 0, 0, 0, 0],
        [-10, 0, -15, -43, 0, -4, 0, 0, 0, 0],
        [0, -15, 0, 0, -7, -5, 0, 0, 0, 0],
        [-9, -43, 0, 0, 0, 0, 0, -46, 0, 0],
        [0, 0, -7, 0, 0, -46, 0, 0, 0, -44],
        [0, -4, -5, 0, -46, 0, -45, 0, -44, -40],
        [0, 0, 0, 0, 0, -45, 0, -21, -48, 0],
        [0, 0, 0, -46, 0, 0, -21, 0, 0, 0],
        [0, 0, 0, 0, 0, -44, -48, 0, 0, -19],
        [0, 0, 0, 0, -44, -40, 0, 0, -19, 0]    
        ]


    matrix = A

    tree = Bellman_Ford_Tree()
    nodes = tree.matrix_build_nodes(matrix)
    tree.build(nodes)
    
    tree._pre_order_list(tree.root)
    

test()
