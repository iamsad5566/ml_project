import unittest
from os import listdir
from FileDir import FileDir

class TestFileDir(unittest.TestCase):
    def testGetFileList(self):
        filePath = "/Users/EupUser/Desktop/py_gain/reading_files"
        self.assertEqual(listdir(filePath), FileDir().getFileList())
        
        
if __name__ == "__main__":
    unittest.main()