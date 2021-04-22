#coding=utf8
#最小生成树
#Kruskal貌似只能用在无向图

class Node:#定好节点的属性
    def __init__(self, name = None, parent = None):
        self.neighbor = []
        self.name = name
        self.children = []
        self.parent = parent
        self.distance = 0 #节点到父节点的距离
        self.edge_count = 0 #节点与树外部连接的边数量
        
class Kruskal_Tree():     
    def __init__(self):
        self.root = None   # 应该有一个根节点
        self.distance_sum = 0 #图的最小路径
        
    def build(self, nodes):
        trees = nodes
        #不会写了

    def matrix_build_nodes(self, matrix): #通过邻接矩阵建立节点集合
        nodes = [] #可以看出是一个森林
        for i in range (len(matrix)): #读每个节点的数据
            node = Node(name=i, parent=None)
            nodes.append(node)
            for j in range (len(matrix)):
                if matrix[i][j] > 0:  #读每个节点的邻近节点
                    node.neighbor.append([j,matrix[i][j]]) #记录邻接点的距离
                    node.edge_count = node.edge_count + 1 #节点与树外部连接的边数量
        return nodes           
    
    def adjList_build_nodes(self, adjList): #通过邻接表建立节点集合
        pass
    
    
    
    def _pre_order_list(self, node):#先序遍历,递归查找
        if node != self.root:
            print("节点 %d 到父节点 %d 的距离是 %d ." %(node.name, node.parent.name, node.distance))
        else:
            print("根节点是 %d." %(node.name))
        if len(node.children) > 0:
            for child in node.children:
                self._pre_order_list(child)    

def test():
    matrix = [
            [0, 6, 0, 32, 0, 0, 0, 0, 0, 0],
            [6, 0, 19, 33, 0, 14, 0, 0, 0, 0],
            [0, 19, 0, 0, 17, 50, 0, 0, 0, 0],
            [32, 33, 0, 0, 0, 0, 0, 49, 0, 0],
            [0, 0, 17, 0, 0, 19, 0, 0, 0, 49],
            [0, 14, 50, 0, 19, 0, 42, 0, 33, 17],
            [0, 0, 0, 0, 0, 42, 0, 37, 7, 0],
            [0, 0, 0, 49, 0, 0, 37, 0, 0, 0],
            [0, 0, 0, 0, 0, 33, 7, 0, 0, 25],
            [0, 0, 0, 0, 49, 17, 0, 0, 25, 0]
            ]
    
    
    tree = Kruskal_Tree()
    nodes = tree.matrix_build_nodes(matrix)
    tree.build(nodes)
    
    #tree._pre_order_list(tree.root)
    print('图的最小路径 %d' %(tree.distance_sum))


test()
