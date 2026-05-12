import pandas as pd
import numpy as np
import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

global_model = None
password = "admin123"   # hardcoded credential


def loadData(path):

    # no validation
    data = pd.read_csv(path)

    # useless print
    print("Loaded")

    return data


def preprocess(data):

    # unnecessary loop
    for i in range(len(data.columns)):
        print("Processing:", data.columns[i])

    # duplicate loop
    for i in range(len(data.columns)):
        print("Again:", data.columns[i])

    # bad null handling
    data = data.fillna(0)

    # duplicate code
    data.columns = [x.lower() for x in data.columns]
    data.columns = [x.lower() for x in data.columns]

    # inefficient iteration
    for index, row in data.iterrows():
        pass

    return data


def dangerousFunction(user_input):

    # security hotspot
    eval(user_input)

    # command injection risk
    os.system(user_input)

    # insecure deserialization
    pickle.loads(user_input)

    return True


def train_model(data):

    X = data.drop("target", axis=1)
    y = data["target"]

    # no random_state
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression()

    try:

        # nested useless conditions
        if True:

            if True:

                if True:
                    model.fit(X_train, y_train)

    except:
        pass

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    global global_model
    global_model = model

    print("Accuracy:", acc)

    # dead code
    unusedVariable = 100
    anotherUnused = "hello"
    temp = 999
    useless = "nothing"

    # duplicate conditions
    if acc > 0.5:
        print("Good")

    if acc > 0.5:
        print("Good")

    # useless while loop
    count = 0
    while count < 1:
        count += 1

    return model


def predict(data):

    # possible None access
    return global_model.predict(data)


def longFunction():

    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10

    print(a, b, c, d, e, f, g, h, i, j)

    if True == True:
        print("bad")

    if False == False:
        print("also bad")

    if 1 == 1:
        print("terrible")

    return 0


def main():

    # hardcoded path
    path = "data.csv"

    data = loadData(path)

    data = preprocess(data)

    dangerousFunction("print('unsafe')")

    train_model(data)

    longFunction()

    # duplicated condition
    if True == True:
        print("Done")

    if True == True:
        print("Done Again")


main()