"""
Benchmarking script to compare slow vs optimized implementations.
This demonstrates the actual performance improvements.
"""

import time
import sys
from functools import wraps


def benchmark(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper


# Import slow implementations
from performance_issues import (
    slow_string_concatenation,
    process_data_with_repeated_computation as process_slow,
    calculate_fibonacci_slow
)

# Import fast implementations
from performance_optimized import (
    fast_string_concatenation,
    process_data_with_cached_computation as process_fast,
    calculate_fibonacci_fast,
    find_common_elements_fast,
    efficient_string_building,
    build_message_fast,
    build_large_string_fast,
    process_data_with_generator,
    squares_with_comprehension,
    count_frequency_fast,
    has_negative_fast
)


def run_benchmarks():
    """Run all benchmarks and display results"""
    print("=" * 80)
    print("PERFORMANCE BENCHMARKS: Slow vs Optimized Code")
    print("=" * 80)
    print()
    
    # Benchmark 1: String concatenation
    print("1. String Concatenation (10,000 iterations)")
    print("-" * 80)
    
    @benchmark
    def test_slow_concat():
        return slow_string_concatenation(10000)
    
    @benchmark
    def test_fast_concat():
        return fast_string_concatenation(10000)
    
    _, slow_time = test_slow_concat()
    _, fast_time = test_fast_concat()
    
    print(f"   Slow (string +=):     {slow_time:.4f} seconds")
    print(f"   Fast (join):          {fast_time:.4f} seconds")
    if fast_time > 0:
        print(f"   Improvement:          {slow_time/fast_time:.2f}x faster")
    else:
        print(f"   Improvement:          instant (fast_time too small to measure)")
    print()
    
    # Benchmark 2: Finding duplicates
    print("2. Finding Duplicates (two lists of 1000 elements)")
    print("-" * 80)
    
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    @benchmark
    def test_find_common():
        return find_common_elements_fast(list1, list2)
    
    _, fast_time = test_find_common()
    print(f"   Fast (using sets):    {fast_time:.6f} seconds")
    print(f"   Note: Slow version would be O(n*m), extremely slow for large lists")
    print()
    
    # Benchmark 3: Fibonacci calculation
    print("3. Fibonacci Calculation (n=30)")
    print("-" * 80)
    
    @benchmark
    def test_slow_fib():
        return calculate_fibonacci_slow(30)
    
    @benchmark
    def test_fast_fib():
        calculate_fibonacci_fast.cache_clear()  # Clear cache for fair comparison
        return calculate_fibonacci_fast(30)
    
    _, slow_time = test_slow_fib()
    _, fast_time = test_fast_fib()
    
    print(f"   Slow (recursive):     {slow_time:.4f} seconds")
    print(f"   Fast (memoized):      {fast_time:.6f} seconds")
    if fast_time > 0:
        print(f"   Improvement:          {slow_time/fast_time:.2f}x faster")
    else:
        print(f"   Improvement:          instant (fast_time too small to measure)")
    print()
    
    # Benchmark 4: Data processing with repeated computation
    print("4. Data Processing with Repeated Computation (10,000 items)")
    print("-" * 80)
    
    data = list(range(10000))
    
    @benchmark
    def test_slow_process():
        return process_slow(data)
    
    @benchmark
    def test_fast_process():
        return process_fast(data)
    
    _, slow_time = test_slow_process()
    _, fast_time = test_fast_process()
    
    print(f"   Slow (recomputing):   {slow_time:.4f} seconds")
    print(f"   Fast (cached):        {fast_time:.4f} seconds")
    if fast_time > 0:
        print(f"   Improvement:          {slow_time/fast_time:.2f}x faster")
    else:
        print(f"   Improvement:          instant (fast_time too small to measure)")
    print()
    
    # Benchmark 5: String building
    print("5. String Building (1000 items)")
    print("-" * 80)
    
    items = list(range(1000))
    
    @benchmark
    def test_string_building():
        return efficient_string_building(items)
    
    _, fast_time = test_string_building()
    print(f"   Fast (join):          {fast_time:.6f} seconds")
    print()
    
    # Benchmark 6: List comprehension
    print("6. List Comprehension vs Loop (100,000 items)")
    print("-" * 80)
    
    @benchmark
    def test_comprehension():
        return squares_with_comprehension(100000)
    
    _, fast_time = test_comprehension()
    print(f"   List comprehension:   {fast_time:.4f} seconds")
    print(f"   Note: List comprehensions are typically 2-3x faster than manual loops")
    print()
    
    # Benchmark 7: Generator for large datasets
    print("7. Generator vs Loading All Data (1,000,000 items)")
    print("-" * 80)
    
    @benchmark
    def test_generator():
        return process_data_with_generator()
    
    result, fast_time = test_generator()
    print(f"   Generator (lazy):     {fast_time:.4f} seconds")
    print(f"   Memory efficient: Only loads what's needed")
    print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("Key Optimization Techniques Demonstrated:")
    print("  1. Use join() instead of string concatenation in loops")
    print("  2. Use sets for O(1) lookups instead of O(n) list searches")
    print("  3. Cache/memoize expensive recursive computations")
    print("  4. Compute values once and reuse (avoid redundant calculations)")
    print("  5. Use list comprehensions instead of manual loops")
    print("  6. Use generators for memory efficiency with large datasets")
    print("  7. Use built-in functions (any, all, sum, etc.) instead of manual loops")
    print("  8. Choose appropriate data structures (Counter, defaultdict, etc.)")
    print("=" * 80)


if __name__ == "__main__":
    run_benchmarks()
