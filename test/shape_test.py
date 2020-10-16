import unittest
from components.shape import Shape


class TestShape(unittest.TestCase):

    def setUp(self):
        self.s1 = Shape(2, 2, '000000')
        self.s2 = Shape(4, 4, '573333')

    def test_add(self):
        s3 = self.s1.add(self.s2)
        self.assertEquals(s3.width, 6)
        self.assertEquals(s3.height, 6)
        self.assertEquals(s3.color, '000000')

    def test_clone(self):
        s3 = self.s1.clone()
        s4 = self.s1
        self.assertTrue(self.s1 == s4)
        self.assertFalse(self.s1 == s3)
