#Tamishia Ayala
#Date: 03/05/2019
#Program to unit test the calculator program
import unittest
import calculator

class TestStringMethods(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(calculator.add(5,2),7)
        self.assertEqual(calculator.add(5,-2),3)
        self.assertEqual(calculator.add(-5,5),0)

    def testSub(self):
        self.assertEqual(calculator.sub(2,5),-3)
        self.assertEqual(calculator.sub(5,-2),3)
        self.assertEqual(calculator.sub(-5,5),-10)

    def testMulti(self):
        self.assertEqual(calculator.multi(5,2),10)
        self.assertEqual(calculator.multi(5,-3),-15)
        self.assertEqual(calculator.multi(-5,3),15)

    def testDiv(self):
        self.assertEqual(calculator.div(10,5),2)
        self.assertEqual(calculator.div(10,-2),-5)
        self.assertEqual(calculator.div(-10,2),-5)

    

    def testPower(self):
        self.assertEqual(calculator.power(2,2),4)
        self.assertEqual(calculator.power(3,3),27)
        self.assertEqual(calculator.power(-4,2),16)

   
        if __name__ == '__main__':
           unittest.main()
