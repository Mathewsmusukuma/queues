from collections import deque

class Queue:
  """
  Basic queue operations using Python
  """
  def __init__(self):
    self.buffer = deque()
    
  def is_empty(self):
    return len(self.buffer) == 0
    
  def enqueue(self, data):
    self.buffer.appendleft(data)
    return None
    
  def dequeue(self): 
    return self.buffer.pop()

  def get_size(self):
    return len(self.buffer)


if __name__ == "__main__":
  q = Queue()
  q.is_empty()
  q.enqueue(3)
  q.dequeue()
  q.get_size()

  