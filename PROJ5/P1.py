import copy


def P1(room):
    '''
    room: M x N list, M>=1, N>=1
    '''
    class fart():
        def __init__(self, room):
            self.now = room
            self.next = copy.deepcopy(room)
            self.M = len(room)
            self.N = len(room[0])
            self.time = 0
            self.done = False
            self.fail = False

        def nearbyGas(self, i, j):
            if self.M > 1:
                if i == 0:
                    if self.now[i + 1][j] == 1:
                        self.next[i][j] = 1
                        self.done = False
                elif i == self.M - 1:
                    if self.now[i - 1][j] == 1:
                        self.next[i][j] = 1
                        self.done = False
                else:
                    if self.now[i + 1][j] == 1 or self.now[i - 1][j] == 1:
                        self.next[i][j] = 1
                        self.done = False

            if self.N > 1:
                if j == 0:
                    if self.now[i][j + 1] == 1:
                        self.next[i][j] = 1
                        self.done = False
                elif j == self.N - 1:
                    if self.now[i][j - 1] == 1:
                        self.next[i][j] = 1
                        self.done = False
                else:
                    if self.now[i][j + 1] == 1 or self.now[i][j - 1] == 1:
                        self.next[i][j] = 1
                        self.done = False

        def fillGas(self):
            while not self.done:
                self.done = True
                for i in range(self.M):
                    for j in range(self.N):
                        if self.now[i][j] == 0:
                            self.nearbyGas(i, j)
                self.now = copy.deepcopy(self.next)
                if self.done == False:
                    self.time = self.time + 1
            for i in range(self.M):
                for j in range(self.N):
                    if self.now[i][j] == 0:
                        self.fail = True

    fartRoom = fart(room)
    fartRoom.fillGas()
    if fartRoom.fail:
        return -1
    else:
        time = fartRoom.time
        return time
    # return type: integer
