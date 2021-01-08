import unittest
import helpers


class TestHelper(unittest.TestCase):

    def setUp(self):
        self.items = [10, 20, 40]

    def test_aggregate(self):
        result = helpers.aggregate(self.items)
        self.assertEqual(result, 70)

    def test_existence(self):
        result = helpers.check_existence(10, self.items)
        self.assertTrue(result, True)


unittest.main()
