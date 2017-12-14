from flask import Flask,jsonify,request,Response
from flask import request
from sklearn import linear_model
import os
import json
import pickle
app = Flask(__name__)
linReg1 = pickle.load(open('predict1.pkl', 'rb'))
linReg2 = pickle.load(open('predict2.pkl', 'rb'))
linReg3 = pickle.load(open('predict3.pkl', 'rb'))
linReg4 = pickle.load(open('predict4.pkl', 'rb'))
linReg5 = pickle.load(open('predict4.pkl', 'rb'))
print('after model loaded')

@app.route('/predict', methods=['POST'])
def get_prediction():
    req_body = request.get_json(force=True)
    param1 = req_body['Size']
    param2 = req_body['Bedrooms']
    param3 = req_body['Age']
    param4 = req_body['Bathrooms']
    param5 = req_body['Price']
    if param1 == '':
        pred = linReg2.predict([[param2, param3, param4,param5]])
        result = pred[0]
        msg = {
            "Predicted size is": " is %s" % (result)
        }
    if param2 == '':
        pred = linReg3.predict([[param1, param3, param4, param5]])
        result = pred[0]
        msg = {
            "Predicted Bedrooms is": " is %s" % (result)
        }
    if param3 == '':
        pred = linReg4.predict([[param1, param2, param4, param5]])
        result = pred[0]
        msg = {
            "Predicted Age of building is": " is %s" % (result)
        }
    if param4 == '':
        pred = linReg5.predict([[param1, param2, param3, param5]])
        result = pred[0]
        msg = {
            "Predicted Bathrooms is": " is %s" % (result)
        }
    else:
        pred = linReg1.predict([[param1, param2, param3, param4]])
        result = pred[0]

    resp = Response(response=json.dumps(msg),
                        status=200,\
                        mimetype="application/json")
    return resp
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0',port=5000)