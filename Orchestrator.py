from flask import Flask, flash, request, redirect, render_template, jsonify
import ExtractionManager as em
import PreprocessingManager as pm
import AnalyticsManager as am


app = Flask(__name__)

connectionApi = None
pathVectorizer = "./static/vectorizer.pkl"
pathCredentials = "./static/credentials.json"
pathModel = "./static/model.sav"


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/analytics', methods=['POST'])
def Analysis():
    global connectionApi
    data_dictionary = request.get_json()
    extractionManager = em.ExtractionManager()
    extractionManager.setCredentials(pathCredentials)
    connectionApi = extractionManager.generateConnection(extractionManager.getCredentials(), connectionApi)
    extractionManager.setDataExtracted(data_dictionary, connectionApi)
    preprocessingManager = pm.PreprocessingManager()
    if extractionManager.getDataExtracted() == []:
        return jsonify({'response': 'Error', 'mensaje': 'Sus términos no arrojaron resultados'})
    preprocessingManager.setDataProcesses(extractionManager.getDataExtracted(), pathVectorizer)
    analyticsManager = am.AnalyticsManager()
    analyticsManager.setDataResulted(preprocessingManager.getDataProcesses(), pathModel)
    return jsonify({'response': 'Success', 'sentimentkeys': analyticsManager.getDataResulted()[0][0],
                    'sentimentvalues': analyticsManager.getDataResulted()[0][1],
                    'tfidfwords': analyticsManager.getDataResulted()[1][0],
                    'tfidfvalues': analyticsManager.getDataResulted()[1][1]})



if __name__ == '__main__':
    app.run(debug=False)

"""
def probarExtaction():
    parameters = {"phrases": [], "account": "", "words": ["Duque"], "hashtags": [], "logicaloption": "AND"}
    global connectionApi
    extractionManager = em.ExtractionManager()
    extractionManager.setCredentials(pathCredentials)
    connectionApi = extractionManager.generateConnection(extractionManager.getCredentials(), connectionApi)
    extractionManager.setDataExtracted(parameters, connectionApi)
    return extractionManager.getDataExtracted()


def probarPreprocessing(tweets, pathvec):
    preprocessingManager = pm.PreprocessingManager()
    preprocessingManager.setDataProcesses(tweets, pathvec)
    return preprocessingManager.getDataProcesses()


def probarAnalytics(pathModel, dataproce):
    analyticsManager = am.AnalyticsManager()
    analyticsManager.setDataResulted(dataproce, pathModel)
    print("----- sentiment -------")
    print(analyticsManager.getDataResulted()[0])
    print("-----------------------")
    print("----- relevant -------")
    print(analyticsManager.getDataResulted()[1])
    print("-----------------------")


a = probarExtaction()

b = probarPreprocessing(a, pathVectorizer)

probarAnalytics(pathModel, b)
"""