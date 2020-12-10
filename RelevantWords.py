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
        dfAux = tfidfmatrix[tfidfmatrix["TF-IDF"] > 0].sort_values('TF-IDF', ascending=False).iloc[:5]
        tfidfValues = dfAux["TF-IDF"].values.tolist()
        tfidfWords = dfAux.index.tolist()
        self._results = [tfidfWords, tfidfValues]

    def getResults(self):
        return self._results
