from collections import deque


def P1(room):
    m = len(room)
    n = len(room[0])
    queue = deque([])
    # 처음 방귀 위치 queue에 넣기
    for i in range(m):
        for j in range(n):
            if room[i][j] == 1:
                # (row 좌표, col 좌표, 시간-1)
                queue.append((i, j, 1))
    # BFS
    while len(queue) != 0:
        node = queue.popleft()
        # 아직 visit하지 않은 곳
        if 0 <= room[node[0]][node[1]] <= 1:
            # 방귀 시간 update
            room[node[0]][node[1]] = node[2]
            # 상하좌우에 대해
            adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i in adj:
                ax = node[0] + i[0]
                ay = node[1] + i[1]
                # 비어있는 공간인 경우에 bfs 진행
                if 0 <= ax < m and 0 <= ay < n and room[ax][ay] == 0:
                    # tuple의 세번째 값에 시간 + 1 을해서 queue에 넣음
                    queue.append((ax, ay, node[2] + 1))
    # 하나라도 0이 있으면 -1을 return
    # 아니면 최대값 return (방귀가 퍼진 마지막 시간)
    ans = 0
    for i in range(m):
        for j in range(n):
            if room[i][j] == 0:
                return -1
            elif room[i][j] > 0:
                ans = max(ans, room[i][j] - 1)
    return ans


def P2(n, edges):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # adjacency matrix
    for e in edges:
        graph[e[0]-1][e[1]-1] = 1
        graph[e[1]-1][e[0]-1] = 1
    visit = [0] * n
    stack = []
    stack.append(0)
    ans = 0
    # dfs
    while len(stack) != 0:
        v = stack.pop()
        if visit[v] == 0:
            ans += 1
            visit[v] = 1
            # neighborhood 중 방문하지 않은 곳 stack에 넣음
            for idx in range(n):
                if graph[v][idx] == 1 and visit[idx] == 0:
                    stack.append(idx)
    return ans


def P3(world):
    m = len(world)
    n = len(world[0])
    ans = 0
    visit = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # 처음 방문한 땅이면 개수 추가
            if world[i][j] == 1 and visit[i][j] == 0:
                ans += 1
                dfs(world, visit, m, n, i, j)
    return ans


def dfs(world, visit, m, n, i, j):
    # 같은 섬의 땅을 dfs로 체크하기
    if 0 <= i < m and 0 <= j < n and world[i][j] == 1 and visit[i][j] == 0:
        visit[i][j] = 1
        dfs(world, visit, m, n, i+1, j)
        dfs(world, visit, m, n, i-1, j)
        dfs(world, visit, m, n, i, j+1)
        dfs(world, visit, m, n, i, j-1)


def P4(L, T):
    visit = [0] * 100001
    queue = deque([])
    # 현재 위치, 시간을 이용
    queue.append((L, 0))
    while(len(queue) != 0):
        loc = queue.popleft()
        if visit[loc[0]] == 0:
            visit[loc[0]] = 1
            # 보물에 도착
            if loc[0] == T:
                return loc[1]
            else:
                move = [loc[0] + 1, loc[0] - 1, 2*loc[0]]
                # 갈 수 있는 위치에 대해 bfs
                for m in move:
                    if 0 <= m <= 100000 and visit[m] == 0:
                        queue.append((m, loc[1] + 1))
