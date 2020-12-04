import pandas as pd
import joblib


class DataTransformation:

    def __init__(self):
        self._vectorizerTransformer = None
        self._dataSentimentAnalysis = None
        self._dataRelevantWords = None
        self._dataTransformed = list()

    def setVectorizerTransformer(self, pathvectorizer):
        self._vectorizerTransformer = joblib.load(pathvectorizer)

    def getVectorizerTransformer(self):
        return self._vectorizerTransformer

    def setDataSentimentAnalysis(self, datacleaned, pathvectorizer):
        self.setVectorizerTransformer(pathvectorizer)
        self._dataSentimentAnalysis = self.getVectorizerTransformer().transform(datacleaned['text'])

    def getDataSentimentAnalysis(self):
        return self._dataSentimentAnalysis

    def setDataRelevantWords(self, datacleaned):
        self._dataRelevantWords = datacleaned['text']

    def getDataRelevantWords(self):
        return self._dataRelevantWords

    def setDataTransformed(self, datacleaned, pathvectorizer):
        self.setDataSentimentAnalysis(datacleaned, pathvectorizer)
        self.setDataRelevantWords(datacleaned)
        self._dataTransformed = [self.getDataSentimentAnalysis(), self.getDataRelevantWords()]

    def getDataTransformed(self):
        return self._dataTransformed
