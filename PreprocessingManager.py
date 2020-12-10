from DataPreparation import DataPreparation
from DataCleaning import DataCleaning
from DataTransformation import DataTransformation


class PreprocessingManager:

    def __init__(self):
        self._dataProcessed = list()
        self._dataPreparation = DataPreparation()
        self._dataCleaning = DataCleaning()
        self._dataTransforming = DataTransformation()

    def setDataProcesses(self, tweets, pathvectorizer):
        self._dataPreparation.setDataPrepared(tweets)
        self._dataCleaning.setDataCleaned(self._dataPreparation.getDataPrepared())
        self._dataTransforming.setDataTransformed(self._dataCleaning.getDataCleaned(), pathvectorizer)
        self._dataProcessed = self._dataTransforming.getDataTransformed()

    def getDataProcesses(self):
        return self._dataProcessed



