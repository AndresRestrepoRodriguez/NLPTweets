import joblib
from collections import Counter
import numpy as np


class SentimentAnalysis:

    def __init__(self):
        self._model = None
        self._predictions = list()
        self._results = dict()

    def setModel(self, path):
        self._model = joblib.load(path)

    def getModel(self):
        return self._model

    def setPredictions(self, dataprocessed, model):
        self._predictions = model.predict(dataprocessed)

    def getPredictions(self):
        return self._predictions

    def setResults(self, predictions):
        replace = lambda x: "Positivo" if x == 1 else ("Neutro" if x == 0 else "Negativo")
        vf = np.vectorize(replace)
        valuesPred = vf(predictions)
        self._results = Counter(valuesPred)

    def getResults(self):
        return self._results
