#Q1:Creating user defined list
from collections import Counter
a=['IBM','SAMSUNG','REDMI']
b=('google','apple','facebook','microsoft','tesla')
a.extend(b)#Q2adding additional item in list
print(a)
print(Counter(a))#Q3-counting the object
#q3create a list get in assending order
m=[2,5,3,1,6,67,87,35,77]
m.sort()
print(m)
#Q5 Given are two one-dimensional arrays A and B which are sorted in
#  ascending order. Write a program to merge them into a single sorted array C
#that contains every item from arrays A and B, in ascending order. [List]
import numpy as np
a = np.array([[1,5,9],[2,6,10]])
b = np.array([[3,7,11],[4,8,12]])
print(np.concatenate((a,b), axis=0))

#question6
#implementing stack using list
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
#implementing queue using list
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)
