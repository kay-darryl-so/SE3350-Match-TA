import pandas as pd


def readApplicationFile(filename):

    applicants = []

    try:                            # trying userInput
        df = pd.read_csv(filename)

    except FileNotFoundError:       # returns "Sorry..." if file does not exist
        print("Sorry, the file you typed in: {}, does not exist".format(filename))
        quit()                      # terminates program

    dict = df.to_dict(orient='list')    # converts dataframe to dictionary of lists

    # Stores each list in the dictionary based on key
    courseCode = dict['Course Code']
    appName = dict['Applicant Name']
    appEmail = dict['applicant email']
    fundable = dict['Applicant status ( 1- Fundable, 2-NotFundable,3-External)']
    numHours = dict['5or10 hrs']
    courseRank = dict['Course Rank']

    sum = 0
    checked = []

    for i in appName:
        if i not in checked:
            j = [appName[sum], appEmail[sum], [(courseCode[sum],courseRank[sum])], fundable[sum], numHours[sum]]
            applicants.append(j)
            checked.append(i)
            sum+=1
        else:
            for k in applicants:
                if str(i) == str(k[0]):
                    k[2].append((courseCode[sum], courseRank[sum]))
                    sum+=1

    return applicants


def getCourses(filename):
    try:                            # trying userInput
        df = pd.read_csv(filename)

    except FileNotFoundError:       # returns "Sorry..." if file does not exist
        print("Sorry, the file you typed in: {}, does not exist".format(filename))
        quit()                      # terminates program

    dict = df.to_dict(orient='list')    # converts dataframe to dictionary of lists

    # Stores each list in the dictionary based on key
    courseCode = dict['Course Code']

    return courseCode

def getFile(filename):

    fileContent = []

    try:                            # trying userInput
        df = pd.read_csv(filename)

    except FileNotFoundError:       # returns "Sorry..." if file does not exist
        print("Sorry, the file you typed in: {}, does not exist".format(filename))
        quit()                      # terminates program

    dict = df.to_dict(orient='list')    # converts dataframe to dictionary of lists

    # Stores each list in the dictionary based on key
    courseCode = dict['Course Code']
    appName = dict['Applicant Name']
    appEmail = dict['applicant email']
    fundable = dict['Applicant status ( 1- Fundable, 2-NotFundable,3-External)']
    numHours = dict['5or10 hrs']
    courseRank = dict['Course Rank']
    q1 = dict['Q1']
    a1 = dict['A1']
    q2 = dict['Q2']
    a2 = dict['A2']
    q3 = dict['Q3']
    a3 = dict['A3']

    sum = 0
    for i in courseCode:
        fileContent.append([i, appName[sum], appEmail[sum], fundable[sum], numHours[sum], courseRank[sum], q1[sum], a1[sum], q2[sum], a2[sum], q3[sum], a3[sum]])
        sum += 1

    return fileContent
