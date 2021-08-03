# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C03-Unit-Testing/05-C03P02

from unittest import TestCase

from interval import Interval


class IntervalTests(TestCase):
    def test_closed_interval_is_inside(self):
        closed_interval = Interval(1, 10)

        self.assertTrue(closed_interval.is_inside(1))
        self.assertTrue(closed_interval.is_inside(5))
        self.assertTrue(closed_interval.is_inside(10))

    def test_closed_interval_stringify(self):
        closed_interval = Interval(1, 10)
        self.assertEqual("[1, 10]", closed_interval.stringify())

    def test_opened_interval_is_inside(self):
        opened_interval = Interval(1, 10, start_opened=True, end_opened=True)

        self.assertFalse(opened_interval.is_inside(1))
        self.assertTrue(opened_interval.is_inside(5))
        self.assertFalse(opened_interval.is_inside(10))

    def test_opened_interval_stringify(self):
        opened_interval = Interval(1, 10, start_opened=True, end_opened=True)
        self.assertEqual("(1, 10)", opened_interval.stringify())

    def test_half_opened_interval_is_inside(self):
        with self.subTest("End opened"):
            half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)

            self.assertTrue(half_opened_interval.is_inside(1))
            self.assertTrue(half_opened_interval.is_inside(5))
            self.assertFalse(half_opened_interval.is_inside(10))

        with self.subTest("Start opened"):
            half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)

            self.assertFalse(half_opened_interval.is_inside(1))
            self.assertTrue(half_opened_interval.is_inside(5))
            self.assertTrue(half_opened_interval.is_inside(10))

    def test_half_opened_interval_strigify(self):
        with self.subTest("End opened"):
            half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)
            self.assertEqual("[1, 10)", half_opened_interval.stringify())

        with self.subTest("Start opened"):
            half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)
            self.assertEqual("(1, 10]", half_opened_interval.stringify())
