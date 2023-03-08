# enQueue 와 deQueue 사용
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data
    
def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0] * 10
front = -1
rear = -1

rear += 1
queue[rear] = 1

enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
    

q = []
q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

from collections import deque
q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())

# 연습문제 1
# 큐를 구현하여 다음 동작을 확인해 봅시다.
# 세 개의 데이터 1,2,3을 차례로 큐에 삽입하고 큐에서 세 개의 데이터를 차례로 꺼내어 출력한다. 1,2,3이 출력 되야 함
