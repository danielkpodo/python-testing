import unittest
import helpers


class TestHelper(unittest.TestCase):

    def setUp(self):
        self.items = [10, 20, 40]

    def tearDown(self):
        pass

    def test_aggregate(self):
        result = helpers.aggregate(self.items)
        self.assertEqual(result, 70)

    def test_existence(self):
        result = helpers.check_existence(10, self.items)
        self.assertTrue(result, True)

    def test_equality(self):
        result = helpers.isEqual(100, 89)
        self.assertFalse(result, False)

    def test_user_email(self):
        test_user = helpers.generate_user_email("narh", "kweku", 27)
        self.assertEqual(test_user, "narhkweku_27@racoondevs.com")


unittest.main()
