from timeit import timeit
import random

class PriorityQueueMergeSort:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self.merge_sort(self.queue)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        for i, current_item in enumerate(self.queue):
            if item < current_item:
                self.queue.insert(i, item)
                return
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

def generate_tasks(n=1000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue',))
    return tasks

def run_tasks(queue, tasks):
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        else:
            queue.dequeue()

task_lists = [generate_tasks() for _ in range(100)]

merge_sort_time = timeit(lambda: [run_tasks(PriorityQueueMergeSort(), tasks) for tasks in task_lists], number=1)
sorted_insert_time = timeit(lambda: [run_tasks(PriorityQueueSortedInsert(), tasks) for tasks in task_lists], number=1)

print(f"Merge Sort Time: {merge_sort_time} seconds")
print(f"Sorted Insert Time: {sorted_insert_time} seconds")

#Q5
''' The significantly faster performance of the priority queue with sorted insert on enqueue highlights its efficiency
for this specific application, especially when compared to the merge sort approach, which requires
 sorting the entire list after each enqueue operation.'''
