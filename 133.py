# coding: utf-8
# Created by bondlee on 2016/6/10


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return

        from collections import deque, defaultdict
        qu, head = deque([]), None
        qu.appendleft(node)
        # 复制节点表
        clone_dic = {}

        # 0为白色， 1为灰色，2为黑色
        node_color = defaultdict(lambda :0)
        node_color[node.label] = 1
        while len(qu):
            n = qu.pop()
            # 节点没有创建过，创建，着灰色
            if n.label not in clone_dic:
                clone_dic[n.label] = UndirectedGraphNode(n.label)
            e = clone_dic[n.label]
            cnei = []
            # 把待复制节点的邻接点创建
            for i in n.neighbors:
                if i.label not in clone_dic:
                    clone_dic[i.label] = UndirectedGraphNode(i.label)
                cnei.append(clone_dic[i.label])
                # 待复制的邻接点进队列
                if not node_color[i.label]:
                    qu.appendleft(i)
                    node_color[i.label] = 1
            # 出队列的节点代表已经创建成功了，此时需要将它们的邻接点补全，相当于着黑色
            node_color[n.label] = 2
            # 复制节点成功
            e.neighbors = cnei
            if not head:
                head = e
        return head

if __name__ == '__main__':
    pass