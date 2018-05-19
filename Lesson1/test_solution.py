from unittest import TestCase
from .lesson1 import solution


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(5, solution(1041))
        self.assertEqual(2, solution(9))
        self.assertEqual(0, solution(1))
        self.assertEqual(0, solution(255))
