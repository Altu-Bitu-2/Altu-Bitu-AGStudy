# 우선순위 큐 (Priority Queue)



## ✏  우선순위 큐란?

일반적인 큐는 First-in-First-out (선입선출) 구조이다. 그러나 우선순위 큐는 **들어간 순서에 상관 없이 우선순위가 높은 데이터가 먼저 나오는 것**을 말한다. 우선순위 큐는 힙(Heap) 자료구조로 구현할 수 있으며, 자료의 루트 노드에 대해서만 모든 연산이 이루어진다. 시간 복잡도는 **O(logn).**

### ---> 힙 (Heap)?

완전 이진트리로, 상위 노드의 값은 모든 하위 노드의 값보다 우선순위가 크거나 같은 특징이 있다. 파이썬에서 힙의 인덱스는 0부터 사용되며, `Min heap`이다.

```python
import heapq

heap = []

# 힙에 값 삽입
heapq.heappush(heap, value)

# 힙에서 값 제거
popped_value = heapq.heappop(heap)

# 새 값을 힙에 삽입하고 pop한 값을 리턴
popped_value = heapq.heappushpop(heap, value)

# 기존 리스트를 heap으로 변경
heapq.heapify(list)
```



### ---> 최대 힙을 만드는 방법

힙에 튜플 원소를 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성된다. 최대 힙을 만들기 위해서는 값의 우선 순위를 구한 후, `(우선순위, 값)` 구조의 튜플을 힙에 추가하거나 삭제하면 된다.

```python
import heapq

num = [1, 2, 3, 4]
heap = []

# 튜플로 입력
for n in num:
	heapq.heappush(heap, (-n, n))

while heap:
	print(heapq.heappop(heap)[1])
```

