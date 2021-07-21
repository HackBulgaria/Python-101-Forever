# interval_tests.py
from unittest import TestCase

from interval import Interval


class IntervalTests(TestCase):
    def test_stringify_produces_correct_result(self):
        interval = Interval(1, 10)
        expected = "[1, 10]"

        self.assertEqual(expected, interval.stringify())

    def test_is_inside_produces_correct_results(self):
        interval = Interval(1, 10)

        self.assertTrue(interval.is_inside(1))
        self.assertTrue(interval.is_inside(5))
        self.assertTrue(interval.is_inside(10))
