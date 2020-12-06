from django.test import TestCase

class DummyTestCase(TestCase):
        def setUp(self):
            pass
        def test_1(self):
            self.assertEqual(11, 11)