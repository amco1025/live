# # i는 값을 결정할 자리, k는 결정할 개수
# def perm(i, k):
#     if i==k:
#         print(*p)
#     else:
#         for j in range(i, k): # 자신의 오른쪽 원소들과 교환
#             p[i], p[j] = p[j], p[i]
#             perm(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
#
# p = [1,2,3,4,5,6]
# perm(0, 3)

# def perm(i, k):
#     if i==k:
#         print(*p)
#     else:
#         for j in range(k): # 사용하지 않은 숫자를
#             if used[j] == 0: # used에서 순서대로 검색
#                 p[i] = A[j]
#                 used[j] = 1
#                 perm(i+1, k)
#                 used[j] = 0
#
# A = [1,4,5]
# p = [0] * 3
# used = [0] * 3
# perm(0, 3)

# # 순열을 만들어 주는 함수
# def perm(i, k):
#     if i == k:
#         # 만약 값이 원하는 길이가 되면 앞 뒤에 시작점과 도착점인 1을 넣고 ans에 추가
#         ans.append([1]+p+[1])
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             perm(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = []
#     # 시작점 1을 제외한 값들을 p에 넣고 순열 만들기
#     for i in range(2, N+1):
#         p.append(i)
#     ans = []
#     perm(0, N-1)
#     mn = 1000000
#     # 만들어진 각 순열들대로 관리구역들을 돌았을 때 전에의 값보다 작으면 최솟값 변경
#     for i in ans:
#         sm = 0
#         for j in range(len(i)-1):
#             sm += arr[i[j]-1][i[j+1]-1]
#         if sm < mn:
#             mn = sm
#
#     print("#"+str(tc)+" "+str(mn))


# i는 값을 결정할 자리, k는 결정할 개수
# def perm(i, k):
#     if i==k:
#         ans.append(p[0:])
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             perm(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     p = list(map(int, input()))
#     ans = []
#     perm(0,len(p))
#
#     sol = 0
#     for i in ans:
#         case = 0
#         if i[0] == i[1] == i[2] or i[0]+2==i[1]+1==i[2]:
#             case += 1
#         if i[3] == i[4] == i[5] or i[3]+2==i[4]+1==i[5]:
#             case += 1
#         if case == 2:
#             sol = 1
#             break
#     print("#"+str(tc)+" "+str(sol))
# # i는 값을 결정할 자리, k는 결정할 개수
#
# def perm(i, k):
#     if i==k:
#         ans.append(p[0:])
#     else:
#         for j in range(i, k): # 자신의 오른쪽 원소들과 교환
#             p[i], p[j] = p[j], p[i]
#             perm(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = []
#     for _ in range(N-1):
#         p.append(1)
#     for _ in range(N-1):
#         p.append(-1)
#     ans = []
#     perm(0,2*N-2)
#     mn = 100000
#     for i in ans:
#         sm = 0
#         a = 0
#         b = 0
#         for j in range(len(i)):
#             if i[j] == 1:
#                 a += 1
#             else:
#                 b += 1
#             sm += arr[a][b]
#             if sm > mn:
#                 break
#
#         if sm < mn:
#             mn = sm
#     mn += arr[0][0]
#     print("#"+str(tc)+" "+str(mn))


# def dfs(n, cnt, sm):
#     global ans
#     if n == N:
#         if cnt==CNT and sm==k:
#             ans += 1
#         return
#     dfs(n+1, cnt+1, sm+lst[n])
#     dfs(n+1, cnt, sm)
#
# T = int(input())
# for tc in range(1, T+1):
#     CNT, k = map(int, input().split())
#
#     N = 12
#     lst = [n for n in range(1, N+1)]
#
#     ans = 0
#     dfs(0,0,0)
#     print(f'#{tc} {ans}')
#
#
# def dfs(i,j,sm):
#     global mn
#     sm += arr[i][j]
#     if i == N-1 and j ==N-1:
#         if sm < mn:
#             mn = sm
#         return
#
#     elif sm > mn:
#         return
#
#     for di, dj in ((1,0),(0,1)):
#         ni = i + di
#         nj = j + dj
#         if ni < N and nj < N:
#             dfs(ni,nj,sm)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     mn = 1000000
#     dfs(0,0,0)
#     print("#"+str(tc)+" "+str(mn))

# from queue import PriorityQueue
# N = int(input())
# pq = PriorityQueue()
#
# for _ in range(N):
#     date = int(input())
#     pq.put(date)
#
# data1 = 0
# data2 = 0
# sum = 0
#
# while pq.qsize()>1:
#     data1 = pq.get()
#     data2 = pq.get()
#     temp = data1 + data2
#     sum += temp
#     pq.put(temp)
#
# print(sum)

# import math
# M, N = map(int, input().split())
# A = [0] * (N + 1)
#
# for i in range(2, N+1):
#     A[i] = i
#
# for i in range(@, int(math.sqrt(N)+1)):

