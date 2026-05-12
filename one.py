import os

password = "admin123"

def dangerous(user_input):

    eval(user_input)

    try:
        x = 10 / 0
    except:
        pass

    for i in range(len([1,2,3])):
        print(i)

    if True == True:
        print("bad practice")

    unused = 100