# Comprehensive Performance Optimization Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Profiling and Measurement](#profiling-and-measurement)
3. [Common Performance Anti-patterns](#common-performance-anti-patterns)
4. [Optimization Techniques](#optimization-techniques)
5. [Real-World Examples](#real-world-examples)

---

## Introduction

Performance optimization is about making your code run faster and use less memory. However, remember:

> "Premature optimization is the root of all evil" - Donald Knuth

**Key Principles:**
- Profile first, optimize second
- Focus on bottlenecks (80/20 rule)
- Measure improvements objectively
- Don't sacrifice readability without good reason

---

## Profiling and Measurement

### Time Complexity Analysis

Understanding Big O notation is crucial:

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Dictionary lookup, array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop through array |
| O(n log n) | Linearithmic | Efficient sorting (merge sort, quick sort) |
| O(n²) | Quadratic | Nested loops |
| O(2^n) | Exponential | Recursive fibonacci without memoization |
| O(n!) | Factorial | Generating all permutations |

### Python Profiling Tools

#### 1. `timeit` - Micro-benchmarking
```python
import timeit

# Time a specific operation
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Time: {time}")
```

#### 2. `cProfile` - Function-level profiling
```python
import cProfile
import pstats

# Profile your code
profiler = cProfile.Profile()
profiler.enable()
your_function()
profiler.disable()

# Print stats
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
```

#### 3. `line_profiler` - Line-by-line profiling
```bash
pip install line_profiler
# Add @profile decorator to functions
kernprof -l -v script.py
```

#### 4. `memory_profiler` - Memory usage
```python
from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a
```

---

## Common Performance Anti-patterns

### 1. String Concatenation in Loops

**❌ Bad:**
```python
result = ""
for i in range(10000):
    result += str(i)  # Creates new string each time
# Time: O(n²)
```

**✅ Good:**
```python
result = "".join(str(i) for i in range(10000))
# Time: O(n)
```

**Why?** Strings are immutable in Python. Each `+=` creates a new string object and copies all previous content.

---

### 2. Using Lists for Membership Testing

**❌ Bad:**
```python
items = [1, 2, 3, 4, 5, ..., 10000]
if 9999 in items:  # O(n) - linear search
    pass
```

**✅ Good:**
```python
items = {1, 2, 3, 4, 5, ..., 10000}  # Use set
if 9999 in items:  # O(1) - hash lookup
    pass
```

**Performance Comparison:**
- List lookup: O(n)
- Set/Dict lookup: O(1)
- For 10,000 items: Set is ~10,000x faster

---

### 3. Repeated Computations

**❌ Bad:**
```python
for i in range(len(data)):
    # len(data) computed every iteration
    process(data[i])
```

**✅ Good:**
```python
length = len(data)  # Computed once
for i in range(length):
    process(data[i])

# Or even better:
for item in data:
    process(item)
```

---

### 4. Naive Recursive Algorithms

**❌ Bad:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# Time: O(2^n) - exponential!
```

**✅ Good - With Memoization:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# Time: O(n) - linear!
```

**✅ Good - Iterative:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
# Time: O(n), Space: O(1)
```

---

### 5. Loading Entire Dataset Into Memory

**❌ Bad:**
```python
def process_large_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())
    # All data in memory!
    return [process(line) for line in data]
```

**✅ Good - Using Generators:**
```python
def process_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield process(line.strip())
    # Lazy evaluation - one line at a time
```

---

### 6. Wrong Algorithm Choice

**❌ Bad - Bubble Sort:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# Time: O(n²)
```

**✅ Good - Use Built-in Sort:**
```python
def sort(arr):
    return sorted(arr)
# Time: O(n log n) - Timsort
```

---

### 7. Inefficient List Operations

**❌ Bad:**
```python
# Deleting from beginning of list
items = list(range(10000))
while items:
    items.pop(0)  # O(n) for each pop!
# Total: O(n²)
```

**✅ Good:**
```python
from collections import deque

items = deque(range(10000))
while items:
    items.popleft()  # O(1) for each pop
# Total: O(n)
```

---

### 8. Not Using Built-in Functions

**❌ Bad:**
```python
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
```

**✅ Good:**
```python
def find_max(numbers):
    return max(numbers)  # Implemented in C, much faster
```

---

## Optimization Techniques

### 1. Use Appropriate Data Structures

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Membership testing | `set` | O(1) lookups |
| Ordered collection | `list` | Index access O(1) |
| Key-value pairs | `dict` | O(1) lookups |
| Queue (FIFO) | `deque` | O(1) append/pop from both ends |
| Priority queue | `heapq` | O(log n) operations |
| Counting | `Counter` | Optimized counting |
| Default values | `defaultdict` | No key checking needed |

### 2. List Comprehensions vs Loops

**Loops:**
```python
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i * i)
```

**List Comprehension (faster):**
```python
result = [i * i for i in range(1000) if i % 2 == 0]
```

**Generator Expression (memory efficient):**
```python
result = (i * i for i in range(1000) if i % 2 == 0)
```

### 3. Local Variable Lookups

**Slow:**
```python
import math
for i in range(1000000):
    result = math.sqrt(i)  # Global lookup each time
```

**Fast:**
```python
from math import sqrt  # Import once
for i in range(1000000):
    result = sqrt(i)  # Local lookup
```

### 4. Avoid Unnecessary Function Calls

**Slow:**
```python
def process_items(items):
    result = []
    for item in items:
        result.append(expensive_function(item))
    return result
```

**Fast (if pure function):**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def expensive_function(x):
    # Computation here
    pass

def process_items(items):
    return [expensive_function(item) for item in items]
```

### 5. Use NumPy for Numerical Operations

**Slow (Pure Python):**
```python
result = []
for i in range(1000000):
    result.append(i * 2 + 5)
```

**Fast (NumPy):**
```python
import numpy as np
result = np.arange(1000000) * 2 + 5
# 10-100x faster!
```

---

## Real-World Examples

### Example 1: Processing Log Files

**❌ Inefficient:**
```python
def analyze_logs(filename):
    errors = []
    warnings = []
    
    # Read entire file into memory
    with open(filename) as f:
        lines = f.readlines()
    
    # Multiple passes through data
    for line in lines:
        if 'ERROR' in line:
            errors.append(line)
    
    for line in lines:
        if 'WARNING' in line:
            warnings.append(line)
    
    return len(errors), len(warnings)
```

**✅ Optimized:**
```python
def analyze_logs(filename):
    error_count = 0
    warning_count = 0
    
    # Stream processing - single pass
    with open(filename) as f:
        for line in f:
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1
    
    return error_count, warning_count
```

**Improvements:**
- Memory: O(1) instead of O(n)
- Single pass instead of two passes
- No list overhead

---

### Example 2: Finding Common Elements

**❌ Inefficient - O(n*m):**
```python
def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common
```

**✅ Optimized - O(n+m):**
```python
def find_common(list1, list2):
    return list(set(list1) & set(list2))
```

**Even Better (preserve order):**
```python
def find_common(list1, list2):
    set2 = set(list2)
    seen = set()
    result = []
    for item in list1:
        if item in set2 and item not in seen:
            result.append(item)
            seen.add(item)
    return result
```

---

### Example 3: Caching API Results

**❌ Without Caching:**
```python
def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Called multiple times for same user_id
data1 = get_user_data(123)
data2 = get_user_data(123)  # Redundant API call
data3 = get_user_data(123)  # Redundant API call
```

**✅ With Caching:**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Only one API call for same user_id
data1 = get_user_data(123)  # API call
data2 = get_user_data(123)  # Cached
data3 = get_user_data(123)  # Cached
```

---

## Performance Testing Checklist

- [ ] Profile code to find actual bottlenecks
- [ ] Analyze time complexity of algorithms
- [ ] Check for repeated computations
- [ ] Verify data structure choices
- [ ] Look for string concatenation in loops
- [ ] Check for nested loops that could be optimized
- [ ] Consider memory usage and leaks
- [ ] Use built-in functions where possible
- [ ] Implement caching for expensive operations
- [ ] Use generators for large datasets
- [ ] Benchmark before and after changes
- [ ] Verify correctness after optimization

---

## Conclusion

Remember:
1. **Profile first** - Don't guess where the bottleneck is
2. **Optimize bottlenecks** - Focus on the slow parts
3. **Measure results** - Verify your optimizations work
4. **Keep it readable** - Don't sacrifice maintainability without good reason
5. **Use the right tool** - Sometimes the best optimization is using a faster library

Happy optimizing! 🚀
