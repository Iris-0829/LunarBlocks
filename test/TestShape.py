import unittest
from components.Shape import Shape


class TestShape(unittest.TestCase):

    def setUp(self):
        self.s1 = Shape(None, '', (200, 200), (5, 5), (0, 0, 0))
        self.s2 = Shape(None, '', (400, 400), (60, 80), (255, 0, 255))

    def test_add(self):
        s3 = self.s1.add(self.s2)
        self.assertEqual(s3.dim, (600, 600))
        self.assertEqual(s3.color, (0, 0, 0))

    def test_clone(self):
        s3 = self.s1.clone()
        s4 = self.s1
        self.assertTrue(self.s1 == s4)
        self.assertFalse(self.s1 == s3)

    def test_equals(self):
        s3 = Shape(None, '', (200, 200), (5, 5), (0, 0, 0))
        self.assertTrue(self.s1.equals(s3))
