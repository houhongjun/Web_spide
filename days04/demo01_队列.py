# -*- coding:utf-8 -*-

#python2中的队列模块
import Queue
#队列的重点：常规队列操作[LILO队列]
#队列的特点：线程安全的。
#1.常规队列LILO队列【FIFO】

q1 = Queue.Queue()

#添加数据：
q1.put("a")
q1.put("b")
q1.put("c")
q1.put("d")
q1.put("e")
q1.put("f")

#打印展示的数据
print (q1.queue)

#队列中获取数据
print("*"*20)
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.queue)
print("*"*20)
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.queue)
#当队列中的数据已经全部获取，再次获取数据时会出现阻塞现象
print ("-"*10)
#2.栈队列

q2 = Queue.LifoQueue()

#添加数据
q2.put("1")
q2.put("2")
q2.put("3")
q2.put("4")
q2.put("5")

#打印数据
print (q2.queue,q2.qsize())

#取出数据
print (q2.get())
print (q2.get())
print (q2.get())
print (q2.queue,q2.qsize())
print (q2.get())
print (q2.get())
# print (q2.get())
# print (q2.queue,q2.qsize())


#3.优先队列：添加的数据在提取时符合一定的优先规则

q3 = Queue.PriorityQueue()

#4.两端队列
q4 = Queue.deque()
q4.append("01")  #从队列的右端添加数据：常规操作
q4.appendleft("90") #从队列的左端添加数据

q4.pop()  #从右端获取数据并移除数据
q4.popleft()#从左端获取数据并移除数据
