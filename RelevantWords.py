from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


class RelevantWords:

    def __init__(self):
        self._tfidfTranformer = None
        self._tfidfMatrix = pd.DataFrame()
        self._results = []

    def setTfidfTransformer(self):
        self._tfidfTranformer = TfidfVectorizer(use_idf=True)

    def getTfidfTransformer(self):
        return self._tfidfTranformer

    def setTfidfMatrix(self, dataprocessed):
        self.setTfidfTransformer()
        newTfIdf = self.getTfidfTransformer().fit_transform(dataprocessed)
        self._tfidfMatrix = pd.DataFrame(newTfIdf[0].T.todense(), index=self.getTfidfTransformer().get_feature_names(), columns=["TF-IDF"])

    def getTfidfMatrix(self):
        return self._tfidfMatrix

    def setResults(self, tfidfmatrix):
        self._results = tfidfmatrix[tfidfmatrix["TF-IDF"] > 0].sort_values('TF-IDF', ascending=False).iloc[:10]

    def getResults(self):
        return self._results