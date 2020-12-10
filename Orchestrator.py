from flask import Flask, flash, request, redirect, render_template, jsonify
import ExtractionManager as em
import PreprocessingManager as pm
import AnalyticsManager as am
import Mailing as ma


app = Flask(__name__)

connectionApi = None
connectionSMTP = None
pathVectorizer = "./static/vectorizer.pkl"
pathCredentials = "./static/credentials.json"
pathModel = "./static/model.sav"
pathPdf = "C:/Users/andre/Downloads/analysis.pdf"



@app.route('/')
def index():
    return render_template('main.html')


@app.route('/analytics', methods=['POST'])
def analysis():
    global connectionApi
    data_dictionary = request.get_json()
    extractionManager = em.ExtractionManager()
    extractionManager.setCredentials(pathCredentials)
    connectionApi = extractionManager.generateConnection(extractionManager.getCredentials(), connectionApi)
    extractionManager.setDataExtracted(data_dictionary, connectionApi)
    preprocessingManager = pm.PreprocessingManager()
    if extractionManager.getDataExtracted() == [] or extractionManager.getDataExtracted() is None:
        return jsonify({'response': 'Error', 'mensaje': 'Sus términos no arrojaron resultados'})
    preprocessingManager.setDataProcesses(extractionManager.getDataExtracted(), pathVectorizer)
    analyticsManager = am.AnalyticsManager()
    analyticsManager.setDataResulted(preprocessingManager.getDataProcesses(), pathModel)
    return jsonify({'response': 'Success', 'sentimentkeys': analyticsManager.getDataResulted()[0][0],
                    'sentimentvalues': analyticsManager.getDataResulted()[0][1],
                    'tfidfwords': analyticsManager.getDataResulted()[1][0],
                    'tfidfvalues': analyticsManager.getDataResulted()[1][1]})


@app.route('/sendmail', methods=['POST'])
def sendmail():
    global connectionSMTP
    data = request.form
    dataDictionary = data.copy()
    emailUser = dataDictionary["emailuser"]
    mailing = ma.Mailing()
    stateMailing = mailing.sendEmail(emailUser, pathPdf, connectionSMTP)
    if stateMailing:
        return jsonify({'response': 'Success'})
    else:
        return jsonify({'response': 'Error'})


if __name__ == '__main__':
    app.run(debug=False)

