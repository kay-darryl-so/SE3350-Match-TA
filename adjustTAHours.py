# Allows Undergraduate Chair to adjust TA hours to each course.

import pandas as pd
import calculateTAHours

def viewHours(filename):

    try:
        df = pd.read_csv(filename, delimiter='\n')

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    try:
        df = pd.read_csv(filename)

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    dict = df.to_dict(orient='list')

    courseCode = dict['Course']
    hours = dict['Hours']

    result = []

    sum = -1
    for c in courseCode:
        sum += 1
        result.append((c, hours[sum]))

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
