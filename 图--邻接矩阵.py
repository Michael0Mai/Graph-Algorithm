#coding=utf8

import random

class MGraph(): #无向图
    def __init__(self):
        self.G = []
        self.Nv = 0 #顶点数
        self.Ne = 0 #边数
    
    def creat(self, datas):
        self.count(datas) #数一下有几个节点
        self.G = [([0] * self.Nv) for i in range(self.Nv)] #创建矩阵,初始值为0
        for data in datas:
            distance = -(random.randint(0, 50)) #随机给边一个权重
            self.G[data[0]][data[1]] = distance
            self.G[data[1]][data[0]] = distance
            
    def count(self, datas):#数一下有几个节点
        count = {}
        for data in datas:
            for i in data[0:2]:
                if i in count.keys():
                    count[i] = count[i] + 1
                else:
                    count[i] = 1
        self.Nv = len(count) #更新节点数
        self.Ne = len(datas) #更新边数
                      
 

def test():

    datas = [ 
            [0,1,1], [0,3,1],
            [1,5,1], [1,3,1], [1,0,1], [1,2,1],
            [2,1,1], [2,5,1], [2,4,1],
            [3,7,1], [3,1,1],
            [4,2,1], [4,5,1], [4,9,1],
            [5,2,1], [5,1,1], [5,4,1], [5,6,1],
            [6,5,1], [6,8,1], [6,7,1],
            [7,6,1],
            [8,9,1], [8,5,1], [8,6,1],
            [9,4,1], [9,5,1], [9,8,1]
            ]
    
    
    mgraph = MGraph()
    mgraph.creat(datas)
    for i in mgraph.G:
        print(i)
        
    
    
test()
