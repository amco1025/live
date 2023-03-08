# 행 우선 순회
for i in range(n):
    for j in range(n):
        Array[i][j]

# 열 우선 순회
for j in range(n):
    for i in range(n):
        Array[i][j]

# 지그재그 순회
for i in range(n):
    for j in range(m):
        Array[i][j + (m -1 -2*j) * (i&2)]

# 델타를 이용한 2차 배열 탐색
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            li[ni][nj]

# 델타 탐색을 이용하여 합

# 전치 행렬
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# 순차 검색 (정렬되어 있지 않은 경우)
def sequentialSearch(a, n, key):
    i = 0
    while i<n and a[i] != key:
        i = i + 1
    if i < n:
        return i
    else:
        return -1

# 순차 검색 (정렬되어 있는 경우)
def sequentialSearch2(a, n, key):
    i = 0
    while i<n and a[i] < key:
        i = i+1
    if i<n and a[i] == key:
        return i
    else:
        return -1

# 이진 검색
def binarySrarch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

# 재귀 함수 이용한 이진 탐색
def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle -2, key)
        elif a[middle] < key:
            return binarySearch2(a, middle + 1, high, key)

# 델타 탐색 기본 예제
T = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ((ni >= 0) & (ni < n)) &  ((nj >= 0) & (nj < n)):
                    answer += abs(li[i][j] - li[ni][nj])
    print("#"+str(tc)+" "+str(answer))
        