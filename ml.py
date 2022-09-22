import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from supTools import SupTools

class MachineLearning():
    def __init__(self, file="test1.csv"):
        self.fileName = SupTools().addPrefix(file)
        
    def getTrainingData(self, learningFactors=[3,5,9]):
        dataSet = pd.read_csv(self.fileName)
        dataSet.head()
        
        y = dataSet.iloc[:, 10].values
        x = dataSet.iloc[:, np.r_[learningFactors]].values 
        return x, y
    
    def dummyCodingNominalVariable(self, x, targetIndex, targetLabel):
        ct = ColumnTransformer([(targetLabel, OneHotEncoder(), [targetIndex])], remainder="passthrough")
        x = ct.fit_transform(x)
        return x[:, 1:]
    
    def getNominalIndexAndLength(self, x, targetIndex, targetLabel, model):
        ct = ColumnTransformer([(targetLabel, OneHotEncoder(), [targetIndex])], remainder="passthrough")
        ct.fit_transform(x)
        namesList = ct.get_feature_names_out()
        n = len(namesList)
        for i in range(n):
            if model == namesList[i].replace(targetLabel+"__x0_", ""):
                return i-1, n
        
        return -1, n
        
    def getLinearRegressor(self, x, y, testRatio=0.2):
        xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=testRatio, random_state=0)
        regressor = LinearRegression()
        regressor.fit(xTrain, yTrain)
        print('Train Score: ', regressor.score(xTrain, yTrain))  
        print('Test Score: ', regressor.score(xTest, yTest))
        return regressor
    
    def generateTestingData(self, x, nominalIndex, nominalLabel, testFactors={"mode":"123"}):
        targetIndex, n = self.getNominalIndexAndLength(x, nominalIndex, nominalLabel, testFactors["model"])
        factorsNum = len(testFactors) - 1
        
        def creatArr(targetIndex, n):
            output = np.array([])
            if targetIndex == -1:
                for i in range((n-factorsNum)-1):
                   output = np.append(output, 0)
                for key in testFactors.keys():
                    if key != "model":
                        output = np.append(output, testFactors[key])
                return output
            
            for i in range(targetIndex):
                output = np.append(output, 0)
            output = np.append(output, 1)
            for i in range((n-factorsNum) - (targetIndex+1) - 1):
                output = np.append(output, 0)
            for key in testFactors.keys():
                if key != "model":
                    output = np.append(output, testFactors[key])
            
            return output
        
        testData = creatArr(targetIndex, n)
        return np.array([testData])