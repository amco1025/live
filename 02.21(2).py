BFS 알고리즘
def BFS(G, v):  # 그래프 G , 탐색 시작점 : v
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            ans.append(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)

    return ans

BFS 알고리즘
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
                visited[i] = visited[n] + 1
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



def BFS(si, sj):  # 그래프 G , 탐색 시작점 : v
    queue = []
    queue.append((si,sj))
    while queue:
        ci, cj = queue.pop(0)
        if visited[ci][cj] == 0:
            visited[ci][cj] = 1
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni = ci + di
                nj = cj + dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1:
                    queue.append((ni,nj))



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                ei, ej = i, j

    BFS(si, sj)
    ans = visited[ei][ej]
    print("#"+str(tc)+" "+str(ans))


그래프 BFS
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

def BFS(graph, v, N): # 그래프와, 시작 값, 노드의 개수를 변수
    q = [v] # 시작 값을 큐에 넣는다.
    visited[v] = 1 # 시작점을 방문 했다고 표시
    while q: # 큐에 값이 존재할 떄까지 반복
        t = q.pop(0) # 큐에서 가장 먼저 들어온 값을 pop하여 t에 입력
        for v in graph[t]: # t에서 갈수 있는 노드들을 v에 넣어가며 반복
            if visited[v] == 0: # 만약 v노드를 방문하지 않았다면
                q.append(v) # 큐에 v노드 추가
                visited[v] = visited[t] + 1 # 방문 표시에 전 방문 값 보다 1추가한 값을 넣어준다.
    return visited

T = 10

for tc in range(1, T+1):
    A, B = map(int, input().split())
    li = list(map(int, input().split()))
    mx = max(li) # 노드의 개수는 리스트에 있는 값 중 가장 큰 값
    graph = [[] for _ in range(mx+1)]
    visited =[0] * (mx+1)

    for i in range(0, len(li), 2): # 그래프 만들기 , 중복 x
        if li[i+1] not in graph[li[i]]:
            graph[li[i]].append(li[i+1])

    answer = BFS(graph, B, mx)

    ans = [(i, answer[i]) for i in range(mx+1)] # ans리스트에 노드의 번호와 그 노드가 몇번만에 방문 되었는지 표시
    final = 0 # 여태 까지 나온 방문 값중 가장 큰 값 나타내줄 변수
    sol = 0 # 그 변수의 인덱스 저장

    for i in range(len(ans)): # 만약 몇 번째로 방문 했는지 보여주는 값이 전 노드들 보다 크다면 sol에 그 리스트 입력 final에 몇 번째로 방문 되었는지 입ㄹ겨
        if ans[i][1] >= final:
            sol = i
            final = ans[i][1]

    print("#"+str(tc)+" "+str(sol))

def BFS(graph, v):
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[v] = visited[t] + 1

    return visited

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    answer = []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N+1):
        answer.append(BFS(graph, i))

    print(answer)

def BFS(graph, v): # 그래프와 시작노드 할당
    q = [v] # 큐에 시작노드 저장
    visited[v] = 1 # 방문리스트 중 시작 노드 인덱스에 1 입력
    while q: # 큐가 존재할 떄 까지 반복
        t = q.pop(0) # 큐에서 가장 먼저 입력된 값을 뽑아 t에 저장
        for i in graph[t]: # t와 연결된 노드들을 i에 넣으며 반복문 진행
            if visited[i] == 0: # 만약 그 노드가 아직 방문 안헀다면
                q.append(i) # 큐에 노드 추가
                visited[i] = visited[t] + 1 # 출발 노드의 방문 인덱스 값보다 1 추가하여 방문 리스트에 저장

    return visited

T = int(input())

for tc in range(1, T+1): # 문제의 조건에 맞추어 그래프와 방문 리스트 만들기
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    A, B = map(int, input().split()) # 시작점과 도착점

    answer = BFS(graph, A)
    if answer[B] != 0:
        ans = answer[B] - 1 # 방문 리스트에서 도착 노드의 인덱스 값에서 1 뺀값 저장
    else:
        ans = 0
    print("#"+str(tc)+" "+str(ans))



def BFS(arr, si, sj):  # 주어진 그래프와 시작 노드 입력
    queue = []
    queue.append((si,sj)) # 큐에 시작 노드 입력
    ci, cj = si, sj
    visited[ci][cj] = 1 # 방문에 1 표시
    while queue: # 큐가 있는 동안 반복
        ci, cj = queue.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)): #4방향 찾기
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1: # 범위 안에 있고 막혀 있지 않다면
                if visited[ni][nj] == 0: # 그 노드가 아직 방문하지 않았다면
                    queue.append((ni,nj)) # 큐에 추가
                    visited[ni][nj] = visited[ci][cj] + 1 # 전 노드의 방문 리스트 값에 1 추가한 값 입력
    return visited



T = int(input())

for tc in range(1, T + 1): # 문제에서 주어진 노드와 간선 graph에 저장
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)] # 몇번에 거쳐 방문했는지 나타낼 리스트 생성

    for i in range(N): # 시작 노드 찾기
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    for i in range(N): # 종료 노드 찾기
        for j in range(N):
            if arr[i][j] == 3:
                ei, ej = i, j

    answer = BFS(arr, si, sj)
    ans = answer[ei][ej]

    if ans != 0:
        ans = ans - 2
    else:
        ans = 0

    print("#"+str(tc)+" "+str(ans))




def BFS(graph, v, N):
    visited = [0] * (N + 1)
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    return visited

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    answer = []

    for _ in range(M):
        a, b = map(int, input().split())
        if b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)

    for i in range(1, N+1):
        answer.append(BFS(graph, i, N))

    ans = 0

    for i in answer:
        for j in i:
            if j > ans:
                ans = j

    print("#"+str(tc)+" "+str(ans))


def dfs(idx, cnt):
    global max
    visit[idx] = True
    if cnt > max:
        max = cnt
    for i in s[idx]:
        if not visit[i]:
            dfs(i, cnt + 1)
            visit[i] = 0


for tc in range(int(input())):
    n, m = map(int, input().split())
    s = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        s[x].append(y)
        s[y].append(x)
    max = 0

    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        dfs(i, 1)
    print('#%d %d' % (tc + 1, max))

# bfs로 다시 풀어보기

def BFS_1(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_1[t] == 0:
            visited_1[t] = 1
            for i in graph_1[t]:
                if visited_1[i] == 0:
                    q.append(i)
    return visited_1

def BFS_2(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_2[t] == 0:
            visited_2[t] = 1
            if visited_1[t] == 1:
                return t
            else:
                for i in graph_1[t]:
                    if visited_2[i] == 0:
                        q.append(i)

def BFS_3(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_3[t] == 0:
            visited_3[t] = 1
            for i in graph_2[t]:
                if visited_3[i] == 0:
                    q.append(i)
    return visited_3


T = int(input())

for tc in range(1, T+1):
    N, M, A, B = map(int, input().split())
    li = list(map(int, input().split()))
    graph_1 = [[] for _ in range(N+1)]
    graph_2 = [[] for _ in range(N+1)]
    visited_1 = [0] * (N+1)
    visited_2 = [0] * (N+1)
    visited_3 = [0] * (N+1)
    answer = 0

    for i in range(0, 2*M, 2):
        graph_1[li[i+1]].append(li[i])

    for i in range(0, 2*M, 2):
        graph_2[li[i]].append(li[i+1])

    BFS_1(A)
    answer = BFS_2(B)
    ans = BFS_3(answer)
    final = 0
    for i in ans:
        if i == 1:
            final += 1

    print(f"#{tc} {answer} {final}")
def DFS(A, B, answer):
    for i in sol:
        if i == 'D':
            A = (2*int(A)) % 10000
            answer.append(i)
            A = str(A)
            if A == B:
                return answer
        elif i == 'S':
            A = int(A) -1
            answer.append(i)
            A = str(A)
            if A == B:
                return answer
        elif i == 'L':
            for j in range(len(A)):
                if j == 0:
                    A[len(A)-1] = A[0]
                    A = str(A)
                    if A == B:
                        return answer
                else:
                    A[j-1] = A[j]
                    A = str(A)
                    if A == B:
                        return answer
        elif i == 'R':
            for j in range(len(A)):
                if j == len(A) - 1:
                    A[0] = A[j]
                    A = str(A)
                    if A == B:
                        return answer
                else:
                    A[j+1] = A[j]
                    A = str(A)
                    if A == B:
                        return answer



T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    sol = ['D', 'S', 'L', 'R']
    answer = []
    print(DFS(A, B, answer))
    print(A)


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    a = 1
    b = 1
    for _ in range(n-1):
        a += 2*i
    for i in range(n-1):
        a += 4*i
    for _ in range(n-1):
        b += 2*i
    for i in range(n):
        b += 4*i

    print(f"#{tc} {a} {b}")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    answer = 0

    while n != 2:
        if n**(1/2) == int(n**(1/2)):
            n = n ** (1/2)
            answer += 1
        else:
            n = n+1
            answer += 1

    print(answer)
def BFS(arr, si, sj):
    queue = []
    queue.append((si,sj))
    ci, cj = si, sj
    visited[ci][cj] = 1
    while queue:
        ci, cj = queue.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] != 1:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
    return visited


T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si, sj = i, j

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 3:
                ei, ej = i, j

    visited = [[0] * 100 for _ in range(100)]

    answer = BFS(arr, si, sj)
    print("#"+str(tc)+" "+str(answer[ei][ej]))