import pandas as pd

def editTAHours(filename, course, hour):

    flag = 0

    try:
        df = pd.read_csv(filename)

    except FileNotFoundError:
        print("Sorry, the file {} does not exist".format(filename))
        quit()

    dict = df.to_dict(orient='list')

    courseCode = dict['Course']
    hours = dict['Hours']

    sum = 0

    for c in courseCode:
        if c == course:
            hours[sum] = hour
            break
        else:
            sum += 1

    with open(filename, 'w') as f:
        f.write('Course,Hours\n')
        a = 0
        for i in courseCode:
            f.write(str(i))
            f.write(',')
            f.write(str(hours[a]))
            f.write('\n')
            a += 1
        f.close()
        flag = 1

    if flag == 0:
        return False
    else:
        return True
