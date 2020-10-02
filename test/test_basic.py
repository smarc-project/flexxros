#!/usr/bin/python3

PKG = 'flexxros'
NAME = 'basic_test'

import sys
import unittest

import rospy
import rostest

from flexx import flx, config
from flexxros import node
from flexxros.node import ROSNode
from flexxros.sam_widgets import SamActuatorBar, SamPlots

class TestBasic(unittest.TestCase):

    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestBasic, sys.argv)
