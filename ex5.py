class CircularQueue:
  """
  A circular queue implementation using an array.
  """

  def __init__(self, capacity):
    """
    Initializes the queue with a fixed capacity.
    """
    self.capacity = capacity
    self.items = [None] * capacity
    self.front = self.rear = -1  # Initialize both pointers to -1

  def is_empty(self):
    """
    Checks if the queue is empty.
    """
    return self.front == -1

  def is_full(self):
    """
    Checks if the queue is full.
    """
    return (self.rear + 1) % self.capacity == self.front

  def enqueue(self, item):
    """
    Adds an item to the queue.
    """
    if self.is_full():
      print("enqueue None")  # Print message for full queue
    else:
      if self.front == -1:
        self.front = 0  # Initialize front for the first element
      self.rear = (self.rear + 1) % self.capacity
      self.items[self.rear] = item
      print(f"enqueue {item}")

  def dequeue(self):
    """
    Removes and returns the front-most item from the queue.
    """
    if self.is_empty():
      print("dequeue None")  # Print message for empty queue
      return None
    else:
      item = self.items[self.front]
      if self.front == self.rear:
        self.front = self.rear = -1  # Reset pointers for single element queue
      else:
        self.front = (self.front + 1) % self.capacity
      print(f"dequeue {item}")
      return item

  def peek(self):
    """
    Returns the front-most item without removing it.
    """
    if self.is_empty():
      print("peek None")  # Print message for empty queue
      return None
    else:
      item = self.items[self.front]
      print(f"peek {item}")
      return item


# Example usage
queue = CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.peek()
queue.dequeue()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)  # Queue is full, won't enqueue
queue.peek()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Queue is empty, won't dequeue
queue.peek()
