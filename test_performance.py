"""
Unit tests for performance optimizations.
Tests verify that optimized versions produce correct results.
"""

import unittest
from performance_issues import (
    slow_string_concatenation,
    process_data_with_repeated_computation,
    calculate_fibonacci_slow
)
from performance_optimized import (
    fast_string_concatenation,
    find_common_elements_fast,
    calculate_fibonacci_fast,
    process_data_with_cached_computation,
    efficient_string_building,
    build_message_fast,
    build_large_string_fast,
    find_duplicates_in_array,
    process_data_with_generator,
    squares_with_comprehension,
    count_frequency_fast,
    has_negative_fast
)


class TestStringOperations(unittest.TestCase):
    """Test string concatenation optimizations"""
    
    def test_string_concatenation_correctness(self):
        """Verify fast version produces same result as slow version"""
        n = 100
        slow_result = slow_string_concatenation(n)
        fast_result = fast_string_concatenation(n)
        self.assertEqual(slow_result, fast_result)
    
    def test_efficient_string_building(self):
        """Test efficient string building"""
        items = [1, 2, 3, 4, 5]
        result = efficient_string_building(items)
        self.assertEqual(result, "1, 2, 3, 4, 5")
    
    def test_build_large_string(self):
        """Test large string building"""
        items = list(range(10))
        result = build_large_string_fast(items)
        expected = ",".join(str(i) for i in range(10))
        self.assertEqual(result, expected)
    
    def test_build_message(self):
        """Test message building"""
        items = ['a', 'b', 'c']
        result = build_message_fast(items)
        self.assertIn("Item: a", result)
        self.assertIn("Item: b", result)
        self.assertIn("Item: c", result)


class TestSetOperations(unittest.TestCase):
    """Test set-based optimizations"""
    
    def test_find_common_elements(self):
        """Test finding common elements in two lists"""
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        result = find_common_elements_fast(list1, list2)
        self.assertEqual(set(result), {3, 4, 5})
    
    def test_find_duplicates_in_array(self):
        """Test finding duplicates in a single array"""
        arr = [1, 2, 3, 2, 4, 3, 5]
        result = find_duplicates_in_array(arr)
        self.assertEqual(set(result), {2, 3})
    
    def test_no_duplicates(self):
        """Test array with no duplicates"""
        arr = [1, 2, 3, 4, 5]
        result = find_duplicates_in_array(arr)
        self.assertEqual(result, [])


class TestFibonacci(unittest.TestCase):
    """Test Fibonacci optimizations"""
    
    def test_fibonacci_correctness(self):
        """Verify fast version produces same result as slow version"""
        for n in range(15):
            calculate_fibonacci_fast.cache_clear()
            self.assertEqual(
                calculate_fibonacci_slow(n),
                calculate_fibonacci_fast(n)
            )
    
    def test_fibonacci_known_values(self):
        """Test against known Fibonacci values"""
        calculate_fibonacci_fast.cache_clear()
        known_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected in enumerate(known_values):
            self.assertEqual(calculate_fibonacci_fast(i), expected)


class TestDataProcessing(unittest.TestCase):
    """Test data processing optimizations"""
    
    def test_cached_computation(self):
        """Test processing with cached computation"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        slow_result = sorted(process_data_with_repeated_computation(data))
        fast_result = sorted(process_data_with_cached_computation(data))
        self.assertEqual(slow_result, fast_result)

    def test_cached_computation_empty_list(self)  self.assertEqual(process_data_with_cached_computation([]), [])
    
    def test_generator_processing(self):
        """Test generator-based processing"""
        result = process_data_with_generator()
        # Verify it's a list
        self.assertIsInstance(result, list)
        # Verify all results are > 100 after processing
        for item in result[:100]:  # Check first 100 items
            self.assertGreater(item, 200)  # item > 100 and then doubled
    
    def test_squares_with_comprehension(self):
        """Test list comprehension for squares"""
        n = 10
        result = squares_with_comprehension(n)
        expected = [i * i for i in range(n)]
        self.assertEqual(result, expected)


class TestUtilityFunctions(unittest.TestCase):
    """Test utility function optimizations"""
    
    def test_count_frequency(self):
        """Test frequency counting"""
        items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = count_frequency_fast(items)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2)
        self.assertEqual(result[3], 3)
        self.assertEqual(result[4], 4)
    
    def test_has_negative_true(self):
        """Test has_negative with negative numbers"""
        numbers = [1, 2, -3, 4, 5]
        self.assertTrue(has_negative_fast(numbers))
    
    def test_has_negative_false(self):
        """Test has_negative without negative numbers"""
        numbers = [1, 2, 3, 4, 5]
        self.assertFalse(has_negative_fast(numbers))
    
    def test_has_negative_empty(self):
        """Test has_negative with empty list"""
        numbers = []
        self.assertFalse(has_negative_fast(numbers))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases"""
    
    def test_empty_lists(self):
        """Test with empty lists"""
        self.assertEqual(find_common_elements_fast([], []), [])
        self.assertEqual(find_common_elements_fast([1, 2], []), [])
        self.assertEqual(find_common_elements_fast([], [1, 2]), [])
    
    def test_single_elements(self):
        """Test with single elements"""
        self.assertEqual(find_common_elements_fast([1], [1]), [1])
        self.assertEqual(find_common_elements_fast([1], [2]), [])
    
    def test_large_numbers(self):
        """Test with large numbers"""
        large_list = list(range(10000))
        result = find_duplicates_in_array(large_list)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
