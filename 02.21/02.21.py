# BFS 알고리즘
def BFS(G, v): # 그래프 G , 탐색 시작점 : v
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
                    
# 연습문제 3
                    
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    vistied = [0] * (V+1)
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
# 각 노드가 몇개의 노드를 거쳐 방문하는지 나타내기
    def bfs(v, N):
    # vistied 생성
    visited = [0] * (N + 1)
    # queue 생성
    q = [v]
    # 시작점 인큐
    visited[v] = 1
    # 시작점 인큐표시
    while q:  # 큐가 비어있지 않으면
        t = q.pop(0)  # 디큐
        print(t, end=' ')  # t에서 처리할 일
        for v in adj[t]:  # t에 인접이고 방문한 적 없는 v
            if visited[v] == 0:
                q.append(v)  # v 인큐
                visited[v] = visited[t] + 1
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adj[n1].append(n2)
    adj[n2].append(n1)
bfs(1, V)  # 시작 정점 : 1 , 마지막 정점 : v





# 

def BFS(G, v, n):
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    return visited

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    ans = []
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(BFS(graph, 1, V))