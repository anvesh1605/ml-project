import os

password = "admin123"

def dangerous(user_input):

    # eval removed - security risk
    # eval(user_input)

    try:
        x = 10 / 0
    except ZeroDivisionError:
        pass

    # Debug loop removed
    # Useless condition removed
    unused = 100