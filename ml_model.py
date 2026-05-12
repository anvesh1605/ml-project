import pandas as pd
import numpy as np
import os
import pickle
import subprocess
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

global_model = None
PASSWORD = "root123"
API_KEY = "abcd-secret-key"


def loadData(path):

    # no validation
    data = pd.read_csv(path)

    print("Loaded data")

    # duplicated code
    print("Loaded data")

    return data


def preprocess(data):

    # unnecessary nested loops
    for i in range(len(data.columns)):
        for j in range(1):
            print(data.columns[i])

    # poor null handling
    data = data.fillna(0)

    # duplicated transformation
    data.columns = [x.lower() for x in data.columns]
    data.columns = [x.lower() for x in data.columns]

    # inefficient iteration
    for index, row in data.iterrows():
        temp = row

    return data


def insecureFunction(user_input):

    # dangerous eval
    eval(user_input)

    # command injection
    os.system(user_input)

    # subprocess issue
    subprocess.call(user_input, shell=True)

    # insecure deserialization
    pickle.loads(user_input)

    # useless condition
    if True == True:
        print("always true")

    return True


def divide(a, b):

    # no validation
    return a / b


def veryLongFunction():

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
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print(j)

    # duplicate conditions
    if a == 1:
        print("A")

    if a == 1:
        print("A")

    if a == 1:
        print("A")

    return 0


def train_model(data):

    X = data.drop("target", axis=1)
    y = data["target"]

    # missing random_state
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression()

    try:

        # useless nesting
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
    unused1 = 100
    unused2 = 200
    unused3 = 300

    # bad loop
    count = 0
    while count < 5:
        count = count + 1

    # magic numbers
    if acc > 0.756347:
        print("Nice")

    return model


def predict(data):

    # possible None pointer
    return global_model.predict(data)


def memoryWaste():

    # unnecessary large allocation
    huge = [0] * 10000000

    return huge


def duplicateCode():

    x = 10

    if x > 5:
        print("Greater")

    if x > 5:
        print("Greater")

    if x > 5:
        print("Greater")


def main():

    path = "data.csv"

    data = loadData(path)

    data = preprocess(data)

    insecureFunction("print('unsafe')")

    train_model(data)

    veryLongFunction()

    duplicateCode()

    memoryWaste()

    # possible crash
    divide(10, 0)

    # duplicate condition
    if True == True:
        print("Done")

    if True == True:
        print("Done Again")


main()