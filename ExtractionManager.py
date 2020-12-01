from datetime import datetime, timedelta
import json
from APIConnection import APIConnection
from Extraction import Extraction


class ExtractionManager:
    def __init__(self):
        self._dates = list()
        self._credentials = dict()

    def setCredentials(self, pathfile):
        with open(pathfile, "r") as read_file:
            self._credentials = json.load(read_file)

    def getCredentials(self):
        return self._credentials

    def setDates(self):
        today = datetime.today()
        dateFormat = "%Y-%m-%d"
        self._dates = [str((today-timedelta(days=val)).strftime(dateFormat)) for val in range(7)]

    def getDates(self):
        return self._dates

    @staticmethod
    def generateConnection(credentials, connection):
        apiconnection = APIConnection(credentials["costumer_key"], credentials["consumer_secret"],
                                      credentials["access_token"], credentials["access_token_secret"])
        auth = apiconnection.setAuthHandler(apiconnection.getCustomerKey(), apiconnection.getCustomerSecret())
        apiconnection.setConnection(auth, apiconnection["access_token"], apiconnection["access_token_secret"], connection)
        return apiconnection.getConnection()

    def generateData(self, parameters, connection):
        extractor = Extraction(parameters["phrases"], parameters["account"], parameters["words"], parameters["hashtags"])
        extractor.setQuery(extractor.getPhrases(), extractor.getWords(), extractor.getHashtags(),
                           extractor.getAccount(), parameters["logicaloption"])
        self.setDates()
        extractor.setTweets(connection, extractor.getQuery(), self.getDates())
        return extractor.getTweets()

