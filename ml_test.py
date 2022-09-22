from cgi import test
import unittest
import pandas as pd
from supTools import SupTools
from ml import MachineLearning
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

class TestML(unittest.TestCase):
    def testGetTrainingData(self):
        file = "test1.csv"
        path = SupTools().addPrefix(file)
        testDataSet = pd.read_csv(path)
        testDataSet.head()
        
        testY = testDataSet.iloc[:, 10].values
        _, y = MachineLearning().getTrainingData()
        self.assertEqual(len(testY), len(y))
        
    def testDummyCodingNominalVariable(self):
        x, _ = MachineLearning().getTrainingData()
        ct = ColumnTransformer([("Model", OneHotEncoder(), [0])], remainder="passthrough")
        testX = x
        
        testX = ct.fit_transform(testX)
        testX = testX[:, 1:]
        x = MachineLearning().dummyCodingNominalVariable(x, 0, "Model")
        self.assertEqual(x.nnz, testX.nnz)
        
    def testGetNominalIndexAndLength(self):
        ml = MachineLearning()
        
        x, _ = ml.getTrainingData()
        index, length = MachineLearning().getNominalIndexAndLength(x, 0, "Model", "DA-JI-SCANIA-B11")
        self.assertNotEqual(-1, index)
        self.assertNotEqual(-1, length)
        
    def testGetLinearRegressor(self):
        ml = MachineLearning()
        
        x, y = ml.getTrainingData()
        dummyX = ml.dummyCodingNominalVariable(x, 0, "Model")
        testRegressor = ml.getLinearRegressor(dummyX, y, 0.2)
        self.assertIsNotNone(testRegressor)
        
    def testGeneratingData(self):
        ml = MachineLearning()
        
        x, _ = ml.getTrainingData()
        testModel = "DA-JI-SCANIA-B11"
        
        index, _ = ml.getNominalIndexAndLength(x, 0, "Model", testModel)
        ct = ColumnTransformer([("Model", OneHotEncoder(), [0])], remainder="passthrough")
        ct.fit_transform(x)
        testIndex = 0
        testNameList = ct.get_feature_names_out()
        for i in range(len(testNameList)):
            if testNameList[i].replace("Model__x0_", "") == testModel:
                testIndex = i-1
                break
              
        self.assertEqual(testIndex, index)
        

        
if __name__ == "__main__":
    unittest.main()