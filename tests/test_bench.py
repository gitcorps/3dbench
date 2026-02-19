import unittest
from src.bench import distance, time_delta


class TestBench(unittest.TestCase):
    def test_distance(self):
        self.assertAlmostEqual(distance((0, 0, 0), (1, 2, 2)), 3.0)

    def test_time_delta(self):
        self.assertEqual(time_delta(5, 2), 3)


if __name__ == "__main__":
    unittest.main()
