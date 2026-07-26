"""
This file demonstrates OPTIMIZED versions of the performance issues.
These implementations are FAST and EFFICIENT.
"""

from functools import lru_cache


# OPTIMIZATION 1: Use join() for string concatenation
def fast_string_concatenation(n=10000):
    """
    Efficient: Using join() with a list
    Time Complexity: O(n)
    """
    return ",".join(str(i) for i in range(n)) + ","


# OPTIMIZATION 2: Use sets for O(1) lookups
def find_common_elements_fast(list1, list2):
    """
    Efficient: O(n+m) complexity using set intersection
    """
    return list(set(list1) & set(list2))


# OPTIMIZATION 3: Efficient string building with join
def efficient_string_building(items):
    """Using join() is much faster than concatenation"""
    return ", ".join(str(item) for item in items)


# OPTIMIZATION 4: Use memoization for recursive functions
@lru_cache(maxsize=None)
def calculate_fibonacci_fast(n):
    """Efficient Fibonacci with memoization - O(n) complexity"""
    if n <= 1:
        return n
    return calculate_fibonacci_fast(n-1) + calculate_fibonacci_fast(n-2)


def process_data_with_cached_computation(data):
    """Efficient: Compute expensive operations once"""
    if not data:
        return []
    average = sum(data) / len(data)  # Computed once
    return [item for item in data if item > average]


# OPTIMIZATION 5: Use sets for O(1) lookups - single array
def find_duplicates_in_array(arr):
    """O(n) algorithm using set - finds duplicates within a single array"""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


# OPTIMIZATION 6: Use join() for string building
def build_message_fast(items):
    """Efficient string building with join"""
    return "".join(f"Item: {item}\n" for item in items)


# OPTIMIZATION 8: Use join() for string concatenation
def build_large_string_fast(items):
    """Efficient string concatenation using join()"""
    return ",".join(str(item) for item in items)


# OPTIMIZATION 9: Modify in-place when possible
def process_data_without_deep_copy(data):
    """Modify data in place instead of deep copying"""
    for item in data:
        item['processed'] = True
    return data


# OPTIMIZATION 10: Use generators for lazy evaluation
def load_data_generator():
    """Generator that yields data on demand"""
    for i in range(1000000):
        yield i * i


def process_data_with_generator():
    """Efficient: uses generator for lazy evaluation"""
    return [item * 2 for item in load_data_generator() if item > 100]


# Additional optimization examples:

# OPTIMIZATION 11: List comprehension vs append in loop
def squares_with_comprehension(n):
    """Efficient: list comprehension is faster"""
    return [i * i for i in range(n)]


def squares_with_loop(n):
    """Less efficient: append in loop"""
    result = []
    for i in range(n):
        result.append(i * i)
    return result


# OPTIMIZATION 12: Use appropriate data structures
def count_frequency_fast(items):
    """Efficient: using Counter from collections"""
    from collections import Counter
    return Counter(items)


def count_frequency_slow(items):
    """Inefficient: manual counting"""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


# OPTIMIZATION 13: Use any() or all() instead of manual loops
def has_negative_fast(numbers):
    """Efficient: using any()"""
    return any(n < 0 for n in numbers)


def has_negative_slow(numbers):
    """Inefficient: manual loop"""
    for n in numbers:
        if n < 0:
            return True
    return False


# OPTIMIZATION 14: Avoid repeated attribute lookups
def process_items_fast(items):
    """Efficient: cache method reference to avoid repeated attribute lookups"""
    result = []
    append_result = result.append  # Cache method reference
    for item in items:
        append_result(item * 2)
    return result
