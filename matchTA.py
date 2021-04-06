# The TA Matching Algorithm

from readApplication import readApplicationFile, getCourses
from funding import getFirstPriority, getSecondPriority, getThirdPriority
from calculateTAHours import calculateHours
from instructorRanking import rankApplicants

def matchTA(filename):

    match = []

    applicants = readApplicationFile(filename)
    first = getFirstPriority(filename)
    second = getSecondPriority(filename)
    third = getThirdPriority(filename)
    profRanking = rankApplicants("InstructorRanking.csv")
    hours = calculateHours("EnrolmentAndHoursSample.csv")
    hoursLeft = {}

    allCourses = getCourses(filename)
    for c in allCourses:
        hoursLeft[c] = hours[findItem(hours, c)][1]


    for applicant in applicants:
        if applicant[0] in first:
            name = applicant[0]
            courses = applicant[2]
            numHours = applicant[4]

            for course in courses:
                rankedPos = findItem(profRanking, course[0])

                if hoursLeft[course[0]] >= numHours and numHours != 0:
                    for i in profRanking[rankedPos][1:]:
                        if name in i[0]:
                            if i[1] == 1 and course[1] == 1:
                                match.append((name, course[0]))
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours

                            elif i[1] == 1 or course[1] == 1:
                                match.append((name, course[0]))
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours
        elif applicant[0] in second:
            name = applicant[0]
            courses = applicant[2]
            numHours = applicant[4]

            for course in courses:
                #hoursPos = findItem(hours, course[0])
                rankedPos = findItem(profRanking, course[0])

                if hoursLeft[course[0]] >= numHours and numHours != 0:
                    for i in profRanking[rankedPos][1:]:
                        if name in i[0]:
                            if i[1] == 1 and course[1] == 1:
                                match.append((name, course[0]))
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours

                            elif i[1] == 1 or course[1] == 1:
                                match.append((name, course[0]))
                                #hoursLeft[course[0]] = hoursLeft[course[0]] - numHours
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours
        else:
            name = applicant[0]
            courses = applicant[2]
            numHours = applicant[4]

            for course in courses:
                rankedPos = findItem(profRanking, course[0])

                if hoursLeft[course[0]] >= numHours and numHours != 0:
                    for i in profRanking[rankedPos][1:]:
                        if name in i[0]:
                            if i[1] == 1 and course[1] == 1:
                                match.append((name, course[0]))
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours

                            elif i[1] == 1 or course[1] == 1:
                                match.append((name, course[0]))
                                sub = hoursLeft[course[0]] - numHours
                                newHours = {course[0]: sub}
                                hoursLeft.update(newHours)
                                numHours = numHours - numHours

    return match


def findItem(theList, item):
    for i in theList:
        if item in i:
            return theList.index(i)
