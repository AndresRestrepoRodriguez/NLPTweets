import numpy as np


class Extraction:

    def __init__(self, phrases, account, words, hashtags):
        self._phrases = phrases
        self._account = account
        self._words = words
        self._hashtags = hashtags
        self._query = list()
        self._tweets = np.array(list())

    def setPhrases(self, phrases):
        self._phrases = phrases

    def setAccount(self, account):
        self._account = account

    def setWords(self, words):
        self._words = words

    def setHashtags(self, hashtags):
        self._hashtags = hashtags

    def setQuery(self, phrases, words, hashtag, account, logicaloption):
        if account == "":
            temporalQuery = phrases + words + hashtag
        else:
            temporalQuery = [account] + phrases + words + hashtag

        if logicaloption == "AND":
            self._query = [' '.join(temporalQuery)]
        else:
            self._query = temporalQuery

    def setTweets(self, connection, query, dates):
        for i in dates:
            for j in query:
                self._tweets = connection.search(q=j, lang="es", count=100, tweet_mode="extended", until=i)

    def getPhrases(self):
        return self._phrases

    def getAccount(self):
        return self._account

    def getWords(self):
        return self._words

    def getHashtags(self):
        return self._hashtags

    def getQuery(self):
        return self._query

    def getTweets(self):
        return self._tweets
