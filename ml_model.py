import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

global_model = None


def loadData(path):
    data = pd.read_csv(path)
    return data


def preprocess(data):

    # unnecessary loop
    for i in range(len(data.columns)):
        print("Processing:", data.columns[i])

    # fill nulls badly
    data = data.fillna(0)

    # duplicate code
    data.columns = [x.lower() for x in data.columns]
    data.columns = [x.lower() for x in data.columns]

    return data


def train_model(data):

    # magic strings
    X = data.drop("target", axis=1)
    y = data["target"]

    # random state missing
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression()

    # broad exception
    try:
        model.fit(X_train, y_train)
    except:
        print("Error happened")

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    # bad global usage
    global global_model
    global_model = model

    print("Accuracy:", acc)

    # dead code
    unusedVariable = 100
    anotherUnused = "hello"

    return model


def predict(data):

    # possible null pointer issue
    return global_model.predict(data)


def main():

    # hardcoded path
    path = "data.csv"

    data = loadData(path)

    data = preprocess(data)

    train_model(data)

    # duplicate condition
    if True == True:
        print("Done")

    if True == True:
        print("Done Again")


main()