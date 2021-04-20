def P2(n, edges):
    '''
    n: integer (>=1)
    edges: list of tuples, len(edges) >= 0
    '''
    class findCluster():
        def __init__(self, edges):
            self.edges = edges
            self.cluster = set()
            self.wait_list = []

        def findFriends(self, v):
            for edge in self.edges:
                if v in edge:
                    if edge[0] == v:
                        if edge[1] not in self.cluster:
                            self.cluster.add(edge[1])
                            self.wait_list.append(edge[1])
                    if edge[1] == v:
                        if edge[0] not in self.cluster:
                            self.cluster.add(edge[0])
                            self.wait_list.append(edge[1])

        def findAll(self):
            self.findFriends(1)
            self.wait_list = list(self.cluster)
            while self.wait_list:
                cur_num = self.wait_list.pop(0)
                self.findFriends(cur_num)
            if 1 in self.cluster:
                return len(self.cluster)
            else:
                return len(self.cluster) + 1

    facebook = findCluster(edges)
    result = facebook.findAll()

    return result

    # return type: integer
