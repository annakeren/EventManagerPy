'''
Created on Apr 29, 2014

@author: Anna
'''
import unittest
from model.Model import selectAllEvents
from model.Model import selectEvent
from model.Model import login
from model.Model import insertEvent
# import model.Model.selectAllEvents
# import model.Model.selectEvent

class Test(unittest.TestCase):


    def setUp(self):
        
        pass


    def tearDown(self):
        pass


    def testName(self):
        responseRead = selectAllEvents()
        print(responseRead)
        responseRead = selectEvent('userName:anna')
        print(responseRead)
        responseRead = login('anna')
        print(responseRead)
        responseRead = insertEvent('event11', 'eventname11', 'cool place', '21:00', '2014:05:17')
        print(responseRead)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()