from os import listdir

class FileDir:
    def __init__(self, path=""):
        self.filePath = "/Users/EupUser/Desktop/py_gain/reading_files"
        if path != "":
            self.filePath = path
        print(path)
        
    def getFileList(self):
        return listdir(self.filePath)
