import unittest

def add( num, *nums):
    # your code here
    # result = 0
    # result += num
    for n in nums:
        num += n
    print(num)
    return num
def subtract( num, *nums):
    # result = 0
    # result -= num 
    for n in nums:
        num -= n
    print(num)
    return num
class MathDojo(unittest.TestCase):
    # def testOne(self):
    #     self.assertEqual(add(2,3,4), 9)
    def testTwo(self):
        self.assertTrue(add(5,6,7) != 20)
    def testThree(self):
        self.assertTrue(subtract(add(5,10),add(2,3)) != 11)
    def setUp(self):
        # DON'T KNOW WHAT THE HINT MEANT BY CREATING AN INSTANCE
        pass
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()