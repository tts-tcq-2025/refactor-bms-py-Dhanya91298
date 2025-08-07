import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertFalse(vitals_ok(99, 102, 70))
        self.assertFalse(vitals_ok(90, 80, 100))
        self.assertFalse(vitals_ok(99, 40, 70))
        self.assertFalse(vitals_ok(99, 105, 70))
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertTrue(vitals_ok(100,80,100))


if __name__ == '__main__':
  unittest.main()




