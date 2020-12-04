import pandas as pd


class DataPreparation:

    def __init__(self):
        self._dataPrepared = pd.DataFrame()

    @staticmethod
    def extractTextTweets(tweets):
        return [tweet.full_text for tweet in tweets]

    @staticmethod
    def textToDataFrame(texttweets):
        return pd.DataFrame(texttweets, columns=["text"])

    def setDataPrepared(self, tweets):
        textTweets = self.extractTextTweets(tweets)
        self._dataPrepared = self.textToDataFrame(textTweets)

    def getDataPrepared(self):
        return self._dataPrepared
