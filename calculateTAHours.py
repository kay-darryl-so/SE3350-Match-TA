# Automates/calculates the number of TA hours to allocate a course based on the data of hours and enrollments
# from the previous year.

import pandas as pd

def calculateHours(filename):
    try:
        df = pd.read_csv(filename)

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    dict = df.to_dict(orient='list')

    courseCode = dict['Course Code']
    #labHours = dict['Lab/tutorial Hours']
    prevEnrollments = dict['Previous Enrollments']
    prevTAHours = dict['Previous TA hours']
    currEnrollments = dict['Current Enrollments']

    TAHours = []

    sum = 0
    for course in courseCode:
        totalHours = (float(prevTAHours[sum]) / float(prevEnrollments[sum])) * float(currEnrollments[sum])
        TAHours.append([course, round(totalHours)])
        sum += 1

    saveResults(TAHours)
    return TAHours


def saveResults(TAHours):
    newFile = '2020-2021.csv'
    with open(newFile, 'w') as f:
        f.write('Course,Hours\n')
        a = 0
        b = 0
        for i in TAHours:
            f.write(str(TAHours[a][b]))
            b += 1
            f.write(',')
            f.write(str(TAHours[a][b]))
            f.write('\n')
            a += 1
            b = 0
        f.close()
