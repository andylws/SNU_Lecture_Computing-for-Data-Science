def P3(world):
    '''
    world: M x N list, M>=1, N>=1
    '''

    class island():
        def __init__(self, world):
            self.world = world
            self.M = len(world)
            self.N = len(world[0])
            self.islDict = {}
            self.size = len(world) * len(world[0])

        def islDictMaking(self):
            for m in range(self.M):
                for n in range(self.N):
                    if self.world[m][n] == 1:
                        self.islDict[m * self.N + n] = []
                        if self.M > 1:
                            if m == 0:
                                if self.world[m + 1][n] == 1:
                                    self.islDict[n].append(
                                        (m + 1) * self.N + n)
                            elif m == self.M - 1:
                                if self.world[m - 1][n] == 1:
                                    self.islDict[m * self.N +
                                                 n].append((m - 1) * self.N + n)
                            else:
                                if self.world[m + 1][n] == 1:
                                    self.islDict[m * self.N + n].append(
                                        (m + 1) * self.N + n)
                                if self.world[m - 1][n] == 1:
                                    self.islDict[m * self.N +
                                                 n].append((m - 1) * self.N + n)
                        if self.N > 1:
                            if n == 0:
                                if self.world[m][n + 1] == 1:
                                    self.islDict[m *
                                                 self.N].append(m * self.N + n + 1)
                            elif n == self.N - 1:
                                if self.world[m][n - 1] == 1:
                                    self.islDict[m * self.N +
                                                 n].append(m * self.N + n - 1)
                            else:
                                if self.world[m][n + 1] == 1:
                                    self.islDict[m *
                                                 self.N + n].append(m * self.N + n + 1)
                                if self.world[m][n - 1] == 1:
                                    self.islDict[m * self.N +
                                                 n].append(m * self.N + n - 1)

        def countIsl(self):
            self.islDictMaking()
            checked = []
            isl_num = 0
            for i in range(self.size):
                if i in self.islDict.keys() and i not in checked:
                    q = [i]
                    while q:
                        cur_num = q.pop(0)
                        for j in self.islDict[cur_num]:
                            if j not in checked:
                                checked.append(j)
                                q.append(j)
                    isl_num = isl_num + 1
            return isl_num

    island = island(world)
    result = island.countIsl()

    return result

    # return type: integer
