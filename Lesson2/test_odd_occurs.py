from unittest import TestCase
from .odd_occurs_in_array import solution
from .odd_occurs_in_array import solution_ver2


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(8, solution_ver2([6, 4, 6, 4, 8]))
        self.assertEqual(7, solution_ver2([9, 3, 9, 3, 9, 7, 9]))
        self.assertEqual(7, solution_ver2([3, 9, 3, 9, 7]))

