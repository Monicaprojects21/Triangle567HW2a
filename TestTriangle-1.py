# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(15, 15, 15), 'Equilateral')

    def testEquilateralTriangle3(self):
        self.assertNotEqual(classifyTriangle(10, 1, 10), 'Equilateral')

    # Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(8, 5, 8), 'Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isosceles')

    # Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(100, 110, 112), 'Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(10, 10, 12), 'Scalene')

    # Testing Invalid Inputs
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle("200", "0", "0"), 'InvalidInput')

    # Testing Not a Triangle
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(1, 5, 1), 'NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(1, 1, 5), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(1, 17, 5), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()