from SentimentAnalysis import SentimentAnalysis
from RelevantWords import RelevantWords


class AnalyticsManager:

    def __init__(self):
        self._dataResulted = list()
        self._sentimentAnalysis = SentimentAnalysis()
        self._relevantWords = RelevantWords()

    def setDataResulted(self, datapro, modelpath):
        self._sentimentAnalysis.setModel(modelpath)
        self._sentimentAnalysis.setPredictions(datapro[0], self._sentimentAnalysis.getModel())
        self._sentimentAnalysis.setResults(self._sentimentAnalysis.getPredictions())
        self._relevantWords.setTfidfMatrix(datapro[1])
        self._relevantWords.setResults(self._relevantWords.getTfidfMatrix())
        self._dataResulted = [self._sentimentAnalysis.getResults(), self._relevantWords.getResults()]

    def getDataResulted(self):
        return self._dataResulted
