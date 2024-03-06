import random
import timeit
import sys
sys.setrecursionlimit(100000)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def build_tree(sorted_array):
    root = None
    for num in sorted_array:
        root = insert(root, num)
    return root

def measure_search_performance(sorted_vector):
    root = build_tree(sorted_vector)

    total_time = 0
    for num in sorted_vector:
        search_time = timeit.timeit(lambda: search(root, num), number=10)
        total_time += search_time

    average_time = total_time / len(sorted_vector)
    return average_time, total_time

# Generate a sorted vector
sorted_vector = list(range(10000))

# Measure search performance on sorted vector
average_time_sorted, total_time_sorted = measure_search_performance(sorted_vector)
print("Performance on sorted vector:")
print("Average search time:", average_time_sorted)
print("Total search time:", total_time_sorted)

# Shuffle the vector
random.shuffle(sorted_vector)

# Measure search performance on shuffled vector
average_time_shuffled, total_time_shuffled = measure_search_performance(sorted_vector)
print("\nPerformance on shuffled vector:")
print("Average search time:", average_time_shuffled)
print("Total search time:", total_time_shuffled)



#Performance on Sorted Vector: Since the tree is constructed from a sorted vector, each member is inserted into it in a way that skews it, thereby producing a linked list. This causes the search time to significantly rise, especially for entries that are close to the vector's end. This stems from the imbalance in the tree, which in the worst scenario turns the search into a linear search.

#Performance on Shuffled Vector: When the components are randomly inserted into the vector before building the tree, a more balanced tree is generated. Therefore, as long as the tree maintains its balanced structure, search speed improves significantly even for components toward the end of the vector.

#In conclusion, compared to the sorted vector strategy, where the tree tends to be significantly skewed, the approach using the shuffled vector is faster since it produces a more balanced tree and so improves search performance.