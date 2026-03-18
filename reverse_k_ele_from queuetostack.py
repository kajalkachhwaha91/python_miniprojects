
import queue


class Queue:
  def __init__(self):
    self.queue = []
    self.stack = []
	
  def qqueue(self, element):
    self.queue.append(element)
	
	
  def reverse_k_ele(self, k):
    if k > len(self.queue):
      return "k is greater than queue size"
    for i in range(k):
      self.stack.append(self.queue.pop(0))
    while self.stack:
      self.queue.append(self.stack.pop())
  
ob = Queue()
ob.qqueue("a")
ob.qqueue("b")
ob.qqueue("c")
print(ob.queue)

print("ob.reverse_k_ele:", ob.reverse_k_ele(2))
print("After reversing first 2 elements:", ob.queue)


