# 버블 정렬
li = [3, 1, 4, 2, 6, 1]
N = len(li)

def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]

BubbleSort(li, N)
print(li)

# 카운팅 정렬
li = [1,2,5,3,2,1,5,4,8,4,2]
mx = max(li)
def counting_sort(array, max): # array는 정렬할 리스트 , max는 정렬할 값중 최대 값
    counting_array = [0] * (max+1) # 각 숫자가 몇개 있는지 나타내 줄 리스트 생성

    for i in array: # 정렬할 리스트의 값을 넣으며 반복문 진행
        counting_array[i] += 1 # 만약 넣은값이 3 이라면 counting_array[3]에 1을 추가

    for i in range(max): # 0 부터 가장 큰 수까지를 i에 넣으며 반복문 진행
        counting_array[i+1] += counting_array[i] # 카운팅 어레이를 합배열 형식으로 만듬

    output_array = [-1]*len(array) # 반환해 줄 리스트 생성

    for i in array: # i에 array값을 넣으며 반복
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array

print(counting_sort(li, mx))

# 선택 정렬
def SelectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

