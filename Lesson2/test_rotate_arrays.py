from unittest import TestCase
from .rotating_arrays import solution


class TestSolution(TestCase):
    def test_solution(self):
        self.assertListEqual([9, 7, 6, 3, 8], solution([3, 8, 9, 7, 6], 3))
        self.assertListEqual([1, 2, 3, 4], solution([1, 2, 3, 4], 4))
        self.assertListEqual([6, 3, 8, 9, 7], solution([3, 8, 9, 7, 6], 1))
        self.assertListEqual([], solution([], 10))
        self.assertListEqual([2], solution([2], 10))
        self.assertListEqual([6, 3, 8, 9, 7], solution([6, 3, 8, 9, 7] , 0))
