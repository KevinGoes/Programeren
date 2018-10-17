import csv


def hoogsteScore():
    with open('behaaldeScoreGamers.csv', 'r') as myCSVFile:
        lezen = csv.reader(myCSVFile, delimiter=';')
        count = 0
        for regel in lezen:
            score = regel[2]
            score = int(score)
            if score > count:
                count = score
                datum = regel[1]
                naam = regel[0]
        return 'De hoogste score is: {} deze score is behaald op {} door {}'.format(count, datum, naam)


print(hoogsteScore())