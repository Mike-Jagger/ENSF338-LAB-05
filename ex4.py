from timeit import timeit
import matplotlib.pyplot as plt
import random

class ArrayQueue:
  """
  Queue implementation using an array.
  """

  def __init__(self):
    self.items = []
    self.front = 0
    self.rear = -1

  def is_empty(self):
    return self.front > self.rear

  def enqueue(self, item):
    self.rear += 1
    self.items.append(item)

  def dequeue(self):
    if self.is_empty():
      return None
    item = self.items[self.front]
    self.front += 1
    return item


class Node:
  """
  Node for the singly linked list.
  """

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedListQueue:
  """
  Queue implementation using a singly linked list.
  """

  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head is None

  def enqueue(self, item):
    new_node = Node(item)
    if self.is_empty():
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def dequeue(self):
    if self.is_empty():
      return None
    item = self.head.data
    self.head = self.head.next
    if self.head is None:
      self.tail = None
    return item


def generate_task_list(n):
  """
  Generates a random list of tasks (enqueue or dequeue operations).
  """
  tasks = []
  for _ in range(n):
    if random.random() < 0.7:
      tasks.append("enqueue")
    else:
      tasks.append("dequeue")
  return tasks


def measure_performance(queue_class, task_list):
    """
    Measures the execution time of performing the tasks on the queue.
    """
    stmt_code = f"q = queue_class()\nfor task in task_list: \n  if task == 'enqueue': \n    q.enqueue(1) \n  else: \n    q.dequeue()"

    # Create the queue instance outside the string
    q = queue_class()

    return timeit(stmt_code, number=100, globals={"q": q})


def main():
  # Generate random task lists
  task_lists = [generate_task_list(10000) for _ in range(100)]

  # Measure performance for array and linked list queues
  array_queue_times = [measure_performance(ArrayQueue, tasks) for tasks in task_lists]
  linked_list_queue_times = [measure_performance(LinkedListQueue, tasks) for tasks in task_lists]

  # Plot the distribution of times
  plt.hist(array_queue_times, label="Array Queue", alpha=0.5)
  plt.hist(linked_list_queue_times, label="Linked List Queue", alpha=0.5)
  plt.xlabel("Time (seconds)")
  plt.ylabel("Frequency")
  plt.title("Performance Comparison of Queue Implementations")
  plt.legend()
  plt.show()


if __name__ == "__main__":
  main()
