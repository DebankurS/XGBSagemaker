import os
import json
import sys
import numpy as np
from xgboost import XGBRanker
from sagemaker_inference import default_handler, model_server

# 1. Load the model from disk
def model_fn(model_dir):
    model = XGBRanker()
    model.load_model(os.path.join(model_dir, "xgbmodelfile.json"))
    return model

# 2. Parse the input request
def input_fn(request_body, content_type):
    if content_type == 'application/json':
        input_json = json.loads(request_body)
        features = input_json.get("features")
        data = np.array(features)
        if len(data.shape) == 1:
            data = data.reshape(1, -1)
        return data
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

# 3. Run inference
def predict_fn(input_data, model):
    predictions = model.predict(input_data)
    return predictions

# 4. Format the output
def output_fn(prediction, accept):
    if accept == 'application/json':
        return json.dumps({"predictions": prediction.tolist()}), 'application/json'
    else:
        raise ValueError(f"Unsupported accept type: {accept}")

# Serve function to start the inference server
def serve():
    # Starts the SageMaker inference server which automatically calls the above functions
    model_server.start_model_server(handler=default_handler.DefaultHandler())

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        serve()
    else:
        print("Usage: python inference.py serve")
