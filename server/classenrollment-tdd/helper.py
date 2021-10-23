import os
import sys
import platform

currentdir = os.path.dirname(os.path.realpath(__file__))
if platform.system() == "Windows":
    parentdir = os.path.dirname(currentdir) + '\\app'
else:
    parentdir = os.path.dirname(currentdir) + '/app'
sys.path.append(parentdir)
# print(sys.path)
# from app import *