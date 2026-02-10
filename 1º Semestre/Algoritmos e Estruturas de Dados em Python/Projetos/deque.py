from collections import deque

s = deque()
print(s)

my_queue = deque([1, 2, 'Name'])
print(my_queue)

my_queue.append('age')
print(my_queue)

my_queue.appendleft('age')
print(my_queue)

my_queue.pop()
print(my_queue)

my_queue.popleft()
print(my_queue)