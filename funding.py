import pandas as pd


def sortPriority(filename):

    try:                            # trying userInput
        df = pd.read_csv(filename)

    except FileNotFoundError:       # returns "Sorry..." if file does not exist
        print("Sorry, the file you typed in: {}, does not exist".format(filename))
        quit()                      # terminates program

    dict = df.to_dict(orient='list')    # converts dataframe to dictionary of lists

    appName = dict['Applicant Name']
    fundable = dict['Applicant status ( 1- Fundable, 2-NotFundable,3-External)']

    #empty lists to store 1st, 2nd and 3rd priority students
    global firstPriority
    firstPriority = []
    global secondPriority
    secondPriority = []
    global thirdPriority
    thirdPriority = []

    #iterates through fundable list to find the index of 1st, 2nd and 3rd priority students and adds to appropriate list
    sum = 0
    for i in fundable:
        if i == 1:
            firstPriority.append(appName[sum])
        elif i == 2:
            secondPriority.append(appName[sum])
        else:
            thirdPriority.append(appName[sum])
        sum +=1

    firstPriority= list(dict.fromkeys(firstPriority))
    secondPriority = list(dict.fromkeys(secondPriority))
    thirdPriority = list(dict.fromkeys(thirdPriority))

def getFirstPriority(filename):
    sortPriority(filename)
    return firstPriority

def getSecondPriority(filename):
    sortPriority(filename)
    return secondPriority

def getThirdPriority(filename):
    sortPriority(filename)
    return thirdPriority
