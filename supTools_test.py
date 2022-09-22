import unittest
import os
from dotenv import load_dotenv
from supTools import SupTools

class TestSupTools(unittest.TestCase):
    def testAddPrefix(self):
        load_dotenv()
        prefix = os.getenv("filePrefix")
        testFileName = "5487.csv"
        self.assertEqual(prefix+testFileName, SupTools().addPrefix(testFileName))
    
    def testMapping(self):
        model = 3
        self.assertEqual(model, SupTools().mappingColumn()["model"])
        
if __name__ == "__main__":
    unittest.main()