"""
#using list to implement queue
queue=[]

queue.append(5)#enqueue
queue.append(-1)
queue.append("Name")
queue.append("a")

print(queue.pop(0))#dequeue
print(queue.pop(0))

print(queue[0])#front

print(len(queue)==0)#Isempty
#using queue dsa

from queue import Queue

q=Queue(maxsize=3)
q.put("How are you")#enqueue
q.put(2)

print(q.get())#dequeue
print(q.get())

q.put("Hi")

print(q.queue[0])#front

print(q.empty())#isempty
print(q.full())

"""
from collections import deque

q=deque()

q.append(1)#add at end
q.append(2)
q.append(3)
print(list(q))
q.appendleft(6)#add at starting
q.appendleft(8)
print(list(q))

q.pop()#delete at end)
q.pop()

print(list(q))

q.popleft()#delete at starting

q.remove(1)#remove 1 from the queue

print(list(q))







