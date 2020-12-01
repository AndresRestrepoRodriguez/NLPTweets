import tweepy
from tweepy import OAuthHandler


class APIConnection():

    def __init__(self, customerkey, customersecret, accesstoken, accesstokensecret, connection):
        self._customerKey = customerkey
        self._customerSecret = customersecret
        self._accessToken = accesstoken
        self._accessTokenSecret = accesstokensecret
        self._auth = None
        self._connection = connection

    def setCustomerKey(self, customerkey):
        self._customerKey = customerkey

    def setCustomerSecret(self, customersecret):
        self._customerSecret = customersecret

    def setAccessToken(self, accesstoken):
        self._accessToken = accesstoken

    def setAccessTokenSecret(self, accesstokensecret):
        self._accessTokenSecret = accesstokensecret

    def setAuthHandler(self, customerkey, customersecret):
        self._auth = OAuthHandler(customerkey, customersecret)

    def setConnection(self, auth, accesstoken, accesstokensecret, connection):
        if connection is None:
            auth.set_access_token(accesstoken, accesstokensecret)
            self._connection = tweepy.API(auth)
        else:
            self._connection = connection

    def getCustomerKey(self):
        return self._customerKey

    def getCustomerSecret(self):
        return self._customerSecret

    def getAccessToken(self):
        return self._accessToken

    def getAccessTokenSecret(self):
        return self._accessTokenSecret

    def getAuthHandler(self):
        return self._auth

    def getConnection(self):
        return self._connection
