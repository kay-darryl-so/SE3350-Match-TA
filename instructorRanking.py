import pandas as pd

def rankApplicants(filename):

    rankedApplicants = []

    try:                            # trying userInput
        df = pd.read_csv(filename)

    except FileNotFoundError:       # returns "Sorry..." if file does not exist
        print("Sorry, the file you typed in: {}, does not exist".format(filename))
        quit()                      # terminates program

    dict = df.to_dict(orient='list')    # converts dataframe to dictionary of lists

    # Stores each list in the dictionary based on key
    name = dict['Name']
    course = dict['Course']
    ranking = dict['Ranking']

    listed = []

    sum = 0
    for i in course:
        if i not in listed:
            rankedApplicants.append([course[sum], (name[sum], ranking[sum])])
            listed.append(i)
            sum = sum + 1
        else:
            for c in rankedApplicants:
                if i == c[0]:
                    if ranking[sum] == 1:
                        c.insert(1, (name[sum], 1))
                        sum = sum + 1
                    elif ranking[sum] == 2:
                        c.insert(2, (name[sum], 2))
                        sum = sum + 1
                    elif ranking[sum] == 3:
                        c.insert(3, (name[sum], 3))
                        sum = sum + 1
                    else:
                        c.append((name[sum], 4))
                        sum = sum + 1

    return rankedApplicants
