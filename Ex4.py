import random
import timeit
import matplotlib.pyplot as plt

# Array-based Queue Implementation
class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

# Singly-Linked List-based Queue Implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return self.head is None

# Task Generation Function
def generate_tasks(n=10000, enqueue_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            tasks.append(('enqueue', random.randint(1, 100)))  # Random value for enqueue
        else:
            tasks.append(('dequeue', None))  # No value needed for dequeue
    return tasks

# Function to Execute Tasks on Queue
def execute_tasks(queue, tasks):
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        elif task[0] == 'dequeue':
            if not queue.is_empty():
                queue.dequeue()

# Performance Measurement Function
def measure_performance(queue_class, task_lists):
    times = []
    for tasks in task_lists:
        queue = queue_class()  # Create a new queue instance for each task list
        start_time = timeit.default_timer()
        execute_tasks(queue, tasks)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    return times

# Generate 100 lists of tasks
task_lists = [generate_tasks() for _ in range(100)]

# Measure performance
array_queue_times = measure_performance(ArrayQueue, task_lists)
linked_list_queue_times = measure_performance(LinkedListQueue, task_lists)

# Plotting Performance Distribution
plt.figure(figsize=(10, 6))
plt.hist(array_queue_times, bins=20, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='LinkedListQueue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Distribution of Queue Implementations')
plt.legend()
plt.grid(True)
plt.show()
