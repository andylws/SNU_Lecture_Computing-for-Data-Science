def P2(n, edges):
    '''
    n: integer (>=1)
    edges: list of tuples, len(edges) >= 0
    '''

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
            for i in range(n):
                if graph[v][i] == 1 and visit[i] == 0:
                    stack.append(i)

    return ans

    # return type: integer
