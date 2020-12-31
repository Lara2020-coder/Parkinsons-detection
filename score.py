import json
import numpy as np
import os
import pickle
import joblib
import pandas as pd

def init():
    global model

    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'best-trained-model-pakinson.pkl')
    model = joblib.load(model_path)

def run(data):
    try:
      
        data = json.loads(data)['data']
        data = pd.DataFrame.from_dict(data)
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})

    except Exception as e:
        error = str(e)
        return json.dumps({"error": error})