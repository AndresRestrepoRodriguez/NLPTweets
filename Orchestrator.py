import ExtractionManager as em
import PreprocessingManager as pm

connectionApi = None
pathVectorizer = "./static/vectorizer.pkl"
pathCredentials = "./static/credentials.json"


def probarExtaction():
    parameters = {"phrases": [], "account": "", "words": ["politica"], "hashtags": [], "logicaloption": "AND"}
    global connectionApi
    extractionManager = em.ExtractionManager()
    credentials = extractionManager.getCredentials()
    extractionManager.setCredentials(pathCredentials)
    connectionApi = extractionManager.generateConnection(extractionManager.getCredentials(), connectionApi)
    extractionManager.setDataExtracted(parameters, connectionApi)
    return extractionManager.getDataExtracted()

def probarPreprocessing(tweets, pathvec):
    preprocessingManager = pm.PreprocessingManager()
    preprocessingManager.setDataProcesses(tweets, pathvec)
    return preprocessingManager.getDataProcesses()


a = probarExtaction()
print(a)
print(len(a))

b = probarPreprocessing(a, pathVectorizer)
print(b)
