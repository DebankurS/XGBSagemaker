import requests
import numpy as np
from sklearn.datasets import load_svmlight_file


test_data = 'testdata/test.txt'
X_test, y_test, qid_test = load_svmlight_file(test_data, query_id=True)

X_test_np=X_test.toarray()


url = "http://localhost:8080/invocations"

for row in X_test_np[:10]:
    
    data = {
        "features":row.tolist()
    }

    response = requests.post(url=url,json=data)
    print(response.json())


row = X_test_np[:5]

data = {
    "features":row.tolist()
}

response = requests.post(url=url,json=data)
response_body = response.json()
print(np.argsort(response_body.get("predictions")))