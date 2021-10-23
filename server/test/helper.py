import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)+ '/app'
# parentdir1 = os.path.dirname(parentdir) + '/app'
# parentdir = os.path.dirname(currentdir) + '\\app'
sys.path.append(parentdir)
# print(sys.path)

from app import *
