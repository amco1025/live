# 이진 검색 알고리즘
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

# 재귀 함수 이용하여 이진 검색
def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
        
        
# 선택 정렬
def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
        