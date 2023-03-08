# def f(i, k, key):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#         if s == key:
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end =' ')
#             print()
#     else:
#         bit[i] = 1
#         f(i+1, k, key)
#         bit[i] = 0
#         f(i+1, k, key)
        
# A = [1,2,3,4,5,6,7,8,9,10]
# N = len(A)
# key = 10
# bit [0]*N
# f(0, N, key)

# 부분집합의 합 1
# def f(i, k, key):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#         if s == key:
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end=' ')
#             print()
#     else:
#         bit[i] = 1
#         f(i + 1, k, key)
#         bit[i] = 0
#         f(i + 1, k, key)
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 10
# bit = [0] * N
# f(0, N, key)

# 부분집합의 합 1
# def f(i, k, key):
#
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#         if s == key:
#             return 1
#         else:
#             return 0
#     else:
#         bit[i] = 1
#         if f(i+1, k, key):
#             return 1
#         bit[i] = 0
#         if f(i+1, k, key):
#             return 1
#         return 0
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 100
# bit = [0] * N
# print(f(0, N, key))

# 부분집합의 합 2

# def f(i, k, s, t): # i원소, k 집합의 크기, s i-1까지 고려된 합, t 찾고자 하는 합
#     global cnt # 찾고자 한느 값을 몇 번 찾았는지
#     global fcnt  # 몇번 재귀를 돌았는지
#     fcnt += 1 # 한번 돌 때마다 1 추가
#     if s > t: # 현재 값이 찾고자하는 값보다 크다면
#         return # 그냥 리턴
#     elif s == t:
#         cnt += 1
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end =" ")
#         print()
#         return
#     elif i == k: # 마지막 원소라면 리턴
#         return
#     else: # 마지막 원소도 아니고 목표 값보다 작다면
#         bit[i] = 1 #
#         f(i+1, k, s+A[i], t)
#         bit[i] = 0
#         f(i+1, k, s, t)
#
#
#
# A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# N = len(A)
# key = 10
# bit = [0] * N
# cnt = 0
# fcnt = 0
#
# f(0,N,0,key)
# print(cnt, fcnt ) # 합이 key인 부분집합의 수

# 만약 1~10까지 있는데 찾는 값이 55라면 어짜피 끝까지 가야한다.
# 이럴 경우 남은 구간의 합 RS라 하면
# S+RS < T 라면 종료

# def su(i, k, s, t):
#     global cnt  # 찾고자 한느 값을 몇 번 찾았는지
#     if s > t:  # 현재 값이 찾고자하는 값보다 크다면
#         return  # 그냥 리턴
#     elif s == t:
#         cnt += 1
#     elif i == k:  # 마지막 원소라면 리턴
#         return
#     else:  # 마지막 원소도 아니고 목표 값보다 작다면
#         bit[i] = 1
#         su(i + 1, k, s + li[i], t)
#         bit[i] = 0
#         su(i + 1, k, s, t)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int,input().split())
#     li = list(map(int, input().split()))
#     cnt = 0
#     bit = [0] * N
#     su(0,N,0,K)
#     print("#"+str(tc)+" "+str(cnt))

# 순열 만들기 1

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# p = [1,2,3]
# f(0, 3)

# 쇠막대기 자르기

# T = int(input())
# for tc in range(1, T+1):
#     sticks = list(map(str, input()))
#     stack = []
#     cnt = 0
#     for i in range(len(sticks)):
#         if sticks[i] =="(":
#             stack.append("(")
#         elif sticks[i] == ")":
#             if sticks[i-1] == "(":
#                 stack.pop()
#                 cnt += len(stack)
#             else:
#                 stack.pop()
#                 cnt+= 1
#     print("#"+str(tc)+" "+str(cnt))

# 분할정복 알고리즘
# 퀵정렬

# def quickSort(a, begin, end):
#     if begin < end:
#         p = partition(a, begin, end)
#         quickSort(a, begin, p-1)
#         quickSort(a, p+1, end)