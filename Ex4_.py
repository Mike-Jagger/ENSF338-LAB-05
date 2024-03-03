import timeit
import random
import matplotlib.pyplot as plt

# Task 1: Implementing ArrayQueue and LinkedListQueue
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()

class LinkedListQueue:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = self.Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.head:
            return None  # Queue is empty
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            self.tail.next = None
        return data

# Task 3: Generate random lists of tasks and print the result
def generate_tasks():
    tasks = []
    for _ in range(10000):
        task = random.choices(['enqueue', 'dequeue'], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

# Task 4: Measure performance of both implementations
def measure_performance(queue_impl, tasks):
    queue = queue_impl()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)  # Dummy data for enqueue operation
        else:
            queue.dequeue()
    end_time = timeit.default_timer()
    return end_time - start_time

# Task 5: Plot the distribution of times and discuss the results
def plot_distribution(array_times, linked_list_times):
    plt.hist(array_times, bins=20, alpha=0.5, label='ArrayQueue')
    plt.hist(linked_list_times, bins=20, alpha=0.5, label='LinkedListQueue')
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Queue Implementation Performance')
    plt.show()

# Task 2: Perform tasks 4 and 5 five times
for _ in range(5):
    array_times = []
    linked_list_times = []
    for _ in range(100):
        tasks = generate_tasks()
        array_time = measure_performance(ArrayQueue, tasks)
        linked_list_time = measure_performance(LinkedListQueue, tasks)
        array_times.append(array_time)
        linked_list_times.append(linked_list_time)

    avg_array_time = sum(array_times) / len(array_times)
    avg_linked_list_time = sum(linked_list_times) / len(linked_list_times)
    print("Average time for ArrayQueue:", avg_array_time)
    print("Average time for LinkedListQueue:", avg_linked_list_time)
    plot_distribution(array_times, linked_list_times)
