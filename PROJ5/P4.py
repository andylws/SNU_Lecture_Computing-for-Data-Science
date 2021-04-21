def P4(L, T):
    '''
    L: current location of Luffy, 0<=L<=100000, integer
    T: location of treasure, 0<=T<=100000, integer
    '''
##########################################################
    ''' First Trial - Partly Failed
    class treasure():
        def __init__(self, L, T):
            self.L = L
            self.T = T

        def DtoB(self, D: int):
            binary = ''
            while D >= 1:
                binary = str(D % 2) + binary
                D = D // 2
            return binary

        def BtoD(self, B: str):
            decimal = 0
            for i in range(len(B)):
                decimal = decimal + int(B[len(B) - i - 1]) * (2 ** i)
            return decimal

        def findTreasure(self):
            if self.L >= self.T:
                return self.L - self.T
            bi_L = self.DtoB(self.L)
            bi_T = self.DtoB(self.T)
            bi_T_cut = bi_T[:len(bi_L)]
            T_cut_dec = self.BtoD(bi_T_cut)
            before_shift_time = abs(T_cut_dec - self.L)
            count_1 = 0
            for i in bi_T[len(bi_L):]:
                count_1 = count_1 + int(i)
            shifting_time = len(bi_T) - len(bi_L) + count_1
            total_time = before_shift_time + shifting_time
            return total_time

    T = treasure(L, T)
    time = T.findTreasure()

    return time
    '''
################################################################
    ''' Second Trial - Almost Totally Failed
    class position():
        def __init__(self, pos):
            self.pos = pos
            self.forward = None
            self.backward = None
            self.jump = None

    class treasure():
        def __init__(self, L, T):
            self.L = L
            self.T = T
            self.last_time = 0
            self.time = 0
            self.checked = []
            self.done = False

        def walkFor(self, cur):
            forward = cur.pos + 1
            cur.forward = position(forward)

        def walkBack(self, cur):
            backward = cur.pos - 1
            cur.backward = position(backward)

        def jumpFor(self, cur):
            jump = cur.pos * 2
            cur.jump = position(jump)

        def possibleMove(self, cur, time, checked):
            if time > self.last_time:
                print(1)
                return
            if cur.pos in checked:
                print(2)
                return
            else:
                checked.append(cur.pos)
                if cur.pos > self.T:
                    print(3)
                    self.walkBack(cur)
                    time = time + 1
                    self.possibleMove(cur.backward, time, checked)
                elif cur.pos < self.T:
                    print(4)
                    self.walkFor(cur)
                    self.walkBack(cur)
                    self.jumpFor(cur)
                    time = time + 1
                    self.possibleMove(cur.forward, time, checked)
                    self.possibleMove(cur.backward, time, checked)
                    self.possibleMove(cur.jump, time, checked)
                elif cur.pos == self.T:
                    print(5)
                    self.time = time
                    self.done = True
                    return

        def findRoute(self):
            while not self.done:
                print(0)
                time = 0
                checked = []
                self.possibleMove(position(self.L), time, checked)
                self.last_time = self.last_time + 1
            print(self.time)
            print(self.last_time)

    movement = treasure(L, T)
    movement.findRoute()

    return
    '''

    class treasure():
        def __init__(self, L, T):
            self.L = L
            self.T = T
            self.layers = []
            self.checked = set()
            self.done = False

        def __findNext(self, cur):
            next_list = []
            if cur > self.T:
                if (cur - 1) not in self.checked:
                    next_list.append(cur - 1)
                    self.checked.add(cur - 1)
                return next_list
            elif cur < self.T:
                if (cur - 1) not in self.checked:
                    next_list.append(cur - 1)
                    self.checked.add(cur - 1)
                if (cur + 1) not in self.checked:
                    next_list.append(cur + 1)
                    self.checked.add(cur + 1)
                if (cur * 2) not in self.checked:
                    next_list.append(cur * 2)
                    self.checked.add(cur * 2)
                return next_list
            elif cur == self.T:
                self.done = True
                return next_list

        def __nextLayer(self):
            layer = []

            for pos in self.layers[-1]:
                layer = layer + self.__findNext(pos)
            self.layers.append(layer)

        def findTreasure(self):
            self.layers.append([self.L])
            while not self.done:
                self.__nextLayer()
            return len(self.layers) - 2

    t = treasure(L, T)
    result = t.findTreasure()

    return result

    # return type: integer
