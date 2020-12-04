import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import unicodedata


class DataCleaning:

    def __init__(self):
        self._dataCleaned = pd.DataFrame()
        nltk.download('stopwords')

    @staticmethod
    def removeEmojis(text):
        emoj = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030""]+", re.UNICODE)
        text = ' '.join([word for word in text.split() if emoj.match(word) is None])
        return text

    @staticmethod
    def toLowerText(text):
        text = text.lower
        return text

    @staticmethod
    def removeUrls(text):
        text = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
        return text

    @staticmethod
    def removePuntuation(text):
        text = "".join(u for u in text if u not in ("¿", "?", ".", ";", ":", "¡", "!", '"', ","))
        return text

    @staticmethod
    def removeStopWords(text):
        stop = stopwords.words('spanish') + ["rt"]
        text = ' '.join([word for word in text.split() if word not in stop])
        return text

    @staticmethod
    def removeExtraCharacters(text):
        text = re.sub('[‘’“”…«»]', '', text)
        return text

    @staticmethod
    def removeAccounts(text):
        text = ' '.join([word for word in text.split() if re.match(r"^@[_a-zA-Z0-9]*", word) is None])
        return text

    @staticmethod
    def removeHashtags(text):
        text = ' '.join([word for word in text.split() if re.match(r"^#[_a-zA-Z0-9]*", word) is None])
        return text

    @staticmethod
    def removeBreakLine(text):
        text = re.sub('\n', ' ', text)
        return text

    @staticmethod
    def removeAccent(text):
        text = unicodedata.normalize('NFD', text) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")
        return str(text)

    def pipeCleaning(self, text):
        text = self.toLowerText(text)
        text = self.removeStopWords(text)
        text = self.removeUrls(text)
        text = self.removeExtraCharacters(text)
        text = self.removeAccounts(text)
        text = self.removeHashtags(text)
        text = self.removeAccent(text)
        text = self.removeBreakLine(text)
        return text

    def defineLambdaPipe(self):
        return lambda x: self.pipeCleaning(x)

    def setDataCleaned(self, dataprepared):
        pipeClean = self.defineLambdaPipe()
        self._dataCleaned = pd.DataFrame(dataprepared["text"].apply(pipeClean))

    def getDataCleaned(self):
        return self._dataCleaned
