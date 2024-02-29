import timeit
import random
import matplotlib.pyplot as plt

# 1.
class ArrayStack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if not self.array:
            return None
        return self.array.pop()

# 2.
class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = ListNode(item, self.head)
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        removed_item = self.head.value
        self.head = self.head.next
        return removed_item

# 3.
def generate_tasks():
    return [('push', random.randint(1, 100)) if random.random() < 0.7 else ('pop', None) for _ in range(10000)]

# 4. 
def measure_performance(stack_class, task_lists):
    times = []
    for tasks in task_lists:
        stack = stack_class()
        start_time = timeit.default_timer()
        for task, item in tasks:
            if task == 'push':
                stack.push(item)
            elif task == 'pop':
                stack.pop()
        times.append(timeit.default_timer() - start_time)
    return times


task_lists = [generate_tasks() for _ in range(100)]

array_stack_times = measure_performance(ArrayStack, task_lists)
linked_list_stack_times = measure_performance(LinkedListStack, task_lists)

for i in range(100):
    print(f'Array Stack Time {i}: {array_stack_times[i]}')
    print(f'Linked List Stack Time {i}: {linked_list_stack_times[i]}')

# 5
plt.figure(figsize=(10, 6))
plt.hist(array_stack_times, alpha=0.5, label='Pythom Array Stack')
plt.hist(linked_list_stack_times, alpha=0.5, label='Singly Linked List Stack')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Comparison of Stack Implementations')
plt.show()

# Discussion
'''
The histogram plots the distribution of execution times for 100 random lists of tasks
for both the array-based and linked-list-based stack implementations.It is
evident that the array-based stack has faster push and pop operations due to direct access
to elements, while the linked-list-based stack shows varied performance depending on
the operation costs of allocating new nodes and updating pointers.
'''
