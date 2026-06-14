"""
This file demonstrates common performance issues in code.
These are examples of SLOW and INEFFICIENT implementations.
"""

import time


# ISSUE 1: Inefficient list concatenation in a loop
def slow_string_concatenation(n=10000):
    """
    Inefficient: Using string concatenation in a loop
    Time Complexity: O(n²) due to string immutability
    """
    result = ""
    for i in range(n):
        result += str(i) + ","
    return result


# ISSUE 2: Nested loops with unnecessary iterations
def find_common_elements_slow(list1, list2):
    """
    Inefficient: O(n*m) complexity for finding common elements
    """
    duplicates = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in duplicates:
                duplicates.append(item1)
    return duplicates


# ISSUE 3: Inefficient string concatenation
def inefficient_string_building(items):
    result = ""
    for item in items:
        result += str(item) + ", "  # Creates new string each iteration
    return result


# ISSUE 4: Repeated expensive computations
def calculate_fibonacci_slow(n):
    """Inefficient recursive Fibonacci - exponential time complexity"""
    if n <= 1:
        return n
    return calculate_fibonacci_slow(n-1) + calculate_fibonacci_slow(n-2)

def process_data_with_repeated_computation(data):
    """Inefficient: Recomputes the same expensive operation multiple times"""
    results = []
    for item in data:
        # Inefficient: Computing sum every iteration
        if item > sum(data) / len(data):
            results.append(item)
    return results

# Issue 5: Poor algorithm choice
def find_duplicates_in_array_slow(arr):
    """O(n²) algorithm for finding duplicates"""
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Issue 6: Inefficient string concatenation
def build_message_slow(items):
    """Inefficient string concatenation in loop"""
    message = ""
    for item in items:
        message += f"Item: {item}\n"  # String concatenation in loop
    return message

# Issue 7: Not using appropriate data structures
def find_duplicates_slow(items):
    """O(n²) complexity using nested loops"""
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

# Issue 8: Inefficient string concatenation
def build_large_string_slow(items):
    result = ""
    for item in items:
        result += str(item) + ","  # String concatenation in loop is O(n²)
    return result[:-1] if result else ""

# Issue 9: Unnecessary deep copying
def process_data_with_deep_copy(data):
    import copy
    results = []
    for item in data:
        # Creating unnecessary deep copies in a loop
        temp = copy.deepcopy(item)
        temp['processed'] = True
        results.append(temp)
    return results

# Issue 10: Not using generators for large datasets
def load_all_data():
    """Loads all data into memory at once"""
    data = []
    for i in range(1000000):
        data.append(i * i)
    return data

def process_all_data():
    """Inefficient: loads everything into memory"""
    data = load_all_data()
    results = []
    for item in data:
        if item > 100:
            results.append(item * 2)
    return results
