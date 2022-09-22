import os
from dotenv import load_dotenv

class SupTools():
    def __init__(self) -> None:
        pass

    def addPrefix(self, file):
        load_dotenv()
        return os.getenv("filePrefix")+file
    
    def mappingColumn(self):
        mp = {"unicode":0, "brand":1, "year":2, "model":3, "type":4, 
              "emission":5, "speedGPS":6, "speedWired":7, "wheelFQ":8, 
              "speedInterval":9, "gain":10}
        
        return mp