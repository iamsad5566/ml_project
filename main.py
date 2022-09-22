from ml import MachineLearning
from supTools import SupTools
import numpy as np

class Execute():
    def __init__(self) -> None:
        # Get Instance (Optional argument: csv path)
        ml = MachineLearning()
        supTool = SupTools()
        
        # Get Training data
        mapping = supTool.mappingColumn()
        learningFactors = np.array([mapping["model"], mapping["emission"], mapping["speedInterval"], mapping["speedGPS"]])
        testFactors = {"model":"DA-JI-SCANIA-B11", "emission":11705, "speedInterval":60, "speedGPS":60} # Should refer to learningFactors
        
        x, y = ml.getTrainingData(learningFactors)
         
        # Transfer nominal variable to dummy coding
        # First parameter: x data set
        # Second parameter: Index of the nominal variable
        # Third parameter: Label of the nominal variable 
        dummyX = ml.dummyCodingNominalVariable(x, 0, "Model")
        
        # Start learning and return the learned regressor
        regressor = ml.getLinearRegressor(dummyX, y, 0.2)

        # Generate a test case
        testCase = ml.generateTestingData(x, 0, "Model", testFactors)
        # Pring the result
        print(regressor.predict(testCase))
        
if __name__ == "__main__":
    Execute()