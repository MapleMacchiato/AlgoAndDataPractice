import unittest
import random
import time
from sorting_algorithms import insertion_sort, merge_sort, quick_sort


class TestSortingAlgorithms(unittest.TestCase):

    def test_insertion_sort(self):
        for i in range(10):
            test_array = []
            number_of_values = random.randint(0, 10000)
            for i in range(number_of_values):
                test_array.append(random.randint(-10000, 10000))
            array_to_test = test_array.copy()
            p_start = time.time()
            test_array.sort()
            p_end = time.time()
            start = time.time()
            sorted_array = insertion_sort(array_to_test)
            end = time.time()
            p_total = round(p_end - p_start, 6)
            total = round(end - start, 6)
            delta = round(p_total-total, 6)
            print(f"Default: {p_total}s, Insertion: {
                  total}s, Delta: {delta}")
            self.assertEqual(test_array, sorted_array)
            self.assertEqual(test_array, sorted_array)

    def test_merge_sort(self):
        for i in range(10):
            test_array = []
            number_of_values = random.randint(0, 10000)
            for i in range(number_of_values):
                test_array.append(random.randint(-10000, 10000))
            array_to_test = test_array.copy()
            p_start = time.time()
            test_array.sort()
            p_end = time.time()
            start = time.time()
            sorted_array = merge_sort(array_to_test)
            end = time.time()
            p_total = round(p_end - p_start, 6)
            total = round(end - start, 6)
            delta = round(p_total-total, 6)
            print(f"Default: {p_total}s, Merge: {
                  total}s, Delta: {delta}")
            self.assertEqual(test_array, sorted_array)

    def test_quick_sort(self):
        for i in range(10):
            test_array = []
            number_of_values = random.randint(0, 10000)
            for i in range(number_of_values):
                test_array.append(random.randint(-10000, 10000))
            array_to_test = test_array.copy()
            p_start = time.time()
            test_array.sort()
            p_end = time.time()
            start = time.time()
            sorted_array = quick_sort(array_to_test)
            end = time.time()
            p_total = round(p_end - p_start, 6)
            total = round(end - start, 6)
            delta = round(p_total-total, 6)
            print(f"Default: {p_total}s, Quick: {
                  total}s, Delta: {delta}")
            self.assertEqual(test_array, sorted_array)
