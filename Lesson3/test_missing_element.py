from unittest import TestCase
from .missing_element import solution


class TestMissingElement(TestCase):
    def test_solution(self):
        self.assertEqual(4, solution([2, 3, 1, 5]))
        self.assertEqual(4, solution([1, 2, 3]))
        self.assertEqual(1, solution([2]))
