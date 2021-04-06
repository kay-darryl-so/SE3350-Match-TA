# Allows Undergraduate Chair to adjust TA hours to each course.

import pandas as pd
import calculateTAHours

def viewHours(filename):

    try:
        df = pd.read_csv(filename, delimiter='\n')

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    global lists
    lists = [list(row) for row in df.values]

    result = ''

    sum = -1
    for i in lists:
        sum += 1
        result = result + str(lists[sum]) + '\n\n'

    return result

def viewList(filename):
    try:
        df = pd.read_csv(filename, delimiter='\n')

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    lists = [list(row) for row in df.values]

    return lists

def adjustHours(filename, course, hours):

    try:
        df = pd.read_csv(filename, delimiter='\n')

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    list1 = [list(row) for row in df.values]

    if course in list1:
        a = list1.index(course)
        list1[a][1] = hours
        df.set_value(a, "Hours", hours)
        df.to_csv(filename, index=False)

    return list1
