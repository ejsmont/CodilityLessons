from unittest import TestCase
from helpers import solve_quadratic_eq


class TestHelpers(TestCase):
    def test_solve_quadratic_eq(self):
        self.assertEqual((-1,), solve_quadratic_eq(1, 2, 1))
        self.assertEqual((3, 5), solve_quadratic_eq(1, -8, 15))
        self.assertEqual(tuple(), solve_quadratic_eq(1, 1, 1))
        self.assertEqual((-2,), solve_quadratic_eq(0, 5, 10))

