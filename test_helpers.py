import unittest
import helpers


class TestHelper(unittest.TestCase):

    def test_aggregate(self):
        items = [10, 20, 30]
        result = helpers.aggregate(items)
        self.assertEqual(result, 60)


unittest.main()
