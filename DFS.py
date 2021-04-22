#coding=utf8

#====================建立树=====================
    
class Node:#定好节点的属性
    def __init__(self, name = None, parent = None):
        self.neighbor = []
        self.name = name
        self.children = []
        self.parent = parent
        self.time_stamp = {'discocvery': 0, 'finish': 0}
        
        

class DFS_Tree():     
    def __init__(self):
        self.root = None   # 应该有一个根节点
        self.time = 0
        
    def build_tree(self, matrix, start_point):
        nodes = self.build_nodes(matrix) #将节点放到一个数列中
        self.root = nodes[start_point] #将源节点定为根节点
        self.search(nodes[start_point], nodes) #从根节点开始搜索
        
    def build_nodes(self, matrix):
        nodes = []
        for i in range (len(matrix)): #读每个节点的数据
            node = Node(name=i, parent=None)
            nodes.append(node)
            for j in range (len(matrix)):
                if matrix[i][j] == 1:  #读每个节点的邻近节点
                    node.neighbor.append(j)
        return nodes
    
    def search(self, node, nodes):
        self.time = self.time + 1
        node.time_stamp['discocvery'] = self.time #记录发现时间
        for near in node.neighbor: #扫描节点里的临界点
            if nodes[near].time_stamp['discocvery'] == 0: #如果邻接点没有被发现
                nodes[near].parent = node #搞定父子关系
                node.children.append(nodes[near])
                self.search(nodes[near], nodes) #递归搜索子节点
        self.time = self.time + 1
        node.time_stamp['finish'] = self.time #记录完成时间
        
    def _pre_order_list(self, node):#先序遍历,递归查找
        print(node.name, node.time_stamp)
        if len(node.children) > 0:
            for child in node.children:
                self._pre_order_list(child)        



#============================测试========================        
def test():

    matrix = [
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 0] 
            ]
    
    
    tree = DFS_Tree()
    start_point = 0
    tree.build_tree(matrix, start_point)
    tree._pre_order_list(tree.root)

test()