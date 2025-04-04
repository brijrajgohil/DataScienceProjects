from flask import Flask, request, jsonify
from joblib
from traceback
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route("/predict", methods=["POST"])

def predict():
    if model:
        try:
            json_ = request.json
            print(_json)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model.predict(query))

            return jsonify({"prediction": str(prediction)})
        except:
            return jsonify({"trace": traceback.format_exc()})
        
    else:
        print("Train the model first")
        return ("No model here to use")
    
@app.route("/show_result", methods=["GET"])
def show_result():
    if model:
        try:
            json_ = [{"pickup_community_area":40, "trip_start_hour":12,"trip_miles":8.3, "trip_seconds":2100,"dropoff_community_area":33}]
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            predict = model.predict(query)
            prediction = list(model.predict(query))
            print(prediction)
            return jsonify({"prediction": str(prediction)})
        except:
            return jsonify({"trace": traceback.format_exc()})
    else:
        print("Train the model first")
        return ("No model here to use")
    
if __name__ =="main":
    try:
        port = int(sys.argv[1])
    except:
        port = 12345

    model_file = "model.pkl"
    model_column_file = model_columns.pkl
    model = joblib.load(model_file)
    print("Model loaded")
    model_columns = joblib.load(model_columns.pkl)
    print("Model columns loaded")
    print(model_columns)
    app.run("0.0.0.0", port=5000)