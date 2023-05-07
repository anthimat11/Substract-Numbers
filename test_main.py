import unittest
from main import subtraction

##unit test method
class TestMain(unittest.TestCase):
    def test(self):
        test1= ["12", "4", "5"]
        self.assertEqual(subtraction(test1), "POSITIVE", "FAILED 1")
        test2 = ["12", "-3", "6", "8"]
        self.assertEqual(subtraction(test2),"NEGATIVE", "FAILED 2")
        test3 = ["23", "4", "45","gdf", "-32"]
        self.assertEqual(subtraction(test3),"NEGATIVE", "FAILED 3")
