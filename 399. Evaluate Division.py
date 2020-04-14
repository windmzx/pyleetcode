from typing import List
class Node:
    def __init__(self):
        self.parent = self
        self.value = 0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def find_parent(node1):
            if node1.parent == node1:
                return node1
            return find_parent(node1.parent)

        def union(node1: Node, node2: Node, value: int, node_map):
            p1 = find_parent(node1)
            p2 = find_parent(node2)
            ratio = node2.value * value/node1.value
            for i in node_map:
                if find_parent(nodemap[i]) == p1:
                    nodemap[i].value=nodemap[i].value*ratio

            p1.parent = p2

        nodemap = {}
        for i in range(len(equations)):
            if equations[i][0] not in nodemap and equations[i][1] not in nodemap:
                nodemap[equations[i][0]] = Node()
                nodemap[equations[i][1]] = Node()
                nodemap[equations[i][0]].value = values[i]
                nodemap[equations[i][1]].value = 1
                nodemap[equations[i][1]].parent = nodemap[equations[i][0]]
            elif equations[i][0] not in nodemap:
                nodemap[equations[i][0]] = Node()
                nodemap[equations[i][0]].value = nodemap[equations[i]
                                                         [1]].value*values[i]
                nodemap[equations[i][0]].parent = nodemap[equations[i][1]]
            elif equations[i][1] not in nodemap:
                nodemap[equations[i][1]] = Node()
                nodemap[equations[i][1]].value = nodemap[equations[i]
                                                         [0]].value/values[i]
                nodemap[equations[i][1]].parent = nodemap[equations[i][0]]
            else:
                union(nodemap[equations[i][0]], nodemap[equations[i][1]], values[i], nodemap)
        res = []
        for query in queries:
            if query[0] in nodemap and query[1] in nodemap and find_parent(nodemap[query[0]]) == find_parent(nodemap[query[1]]):
                res.append(nodemap[query[0]].value/nodemap[query[1]].value)
            else:
                res.append(-1)
        return res
if __name__ == "__main__":
    x=Solution()
    x.calcEquation(
        [["a","b"],["e","f"],["b","e"]],[3.4,1.4,2.3],[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
    )