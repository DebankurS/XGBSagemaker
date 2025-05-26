import os
from xgboost import XGBRanker
import numpy as np
from sklearn.datasets import load_svmlight_file


def load_data(file_path):
    X, y, qid = load_svmlight_file(file_path, query_id=True)
    _, counts = np.unique(qid, return_counts=True)
    group = counts.tolist()

    return X, y, group


if __name__ == "__main__":
    train_path =  "/opt/ml/input/data/train/train.txt"
    validation_path = "/opt/ml/input/data/validation/vali.txt"
    model_dir = "/opt/ml/model"

    X_train, y_train, group_train = load_data(train_path)

    ranker = XGBRanker(objective="rank:pairwise", n_jobs=-1)

    ranker.fit(X_train, y_train, group=group_train, verbose=True)

    ranker.save_model(os.path.join(model_dir, "xgbmodelfile.json"))
