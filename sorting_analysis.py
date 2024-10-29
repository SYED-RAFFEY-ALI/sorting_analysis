import time
import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure time taken by each sort function
def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        sorted_arr = sort_function(arr)
    else:
        sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Define array sizes
n = 1000

# Best case scenario: sorted array
array_best = list(range(1, n+1))

# Average case scenario: randomly shuffled array
array_avg = array_best[:]
random.shuffle(array_avg)

# Worst case scenario: descending order
array_worst = list(range(n, 0, -1))

# Dictionary to hold results
results = {}

# Clone the arrays to keep the original order in each test
arrays = {
    "Best Case": array_best[:],
    "Average Case": array_avg[:],
    "Worst Case": array_worst[:]
}

for case, array in arrays.items():
    results[case] = {}
    # Clone arrays for each sorting algorithm to ensure they sort identical lists
    results[case]["Bubble Sort"] = measure_time(bubble_sort, array[:])
    results[case]["Selection Sort"] = measure_time(selection_sort, array[:])
    results[case]["Merge Sort"] = measure_time(merge_sort, array[:])
    results[case]["Quick Sort"] = measure_time(quick_sort, array[:])

# Print the results
print("Execution Time (in seconds) for Each Sorting Algorithm and Array:")
for case, timings in results.items():
    print(f"\n{case}:")
    for algorithm, time_taken in timings.items():
        print(f"  {algorithm}: {time_taken:.6f} seconds")
