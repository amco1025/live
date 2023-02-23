# 트리의 정점 표시하기
# 13
# 1 2 1 3 ....
def preorder(i):
    if i > 0:
        print(i, end = ' ')
        preorder(left[i])
        preorder(right[i])
    return
        

V = int(input())
arr = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)
par = [0] * (V+1)
#child =  [[] for _ in range(V+1)]

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    
    par[c] = p

root =0
while par[root] != 0:
    root += 1
preorder(root)
