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
        print('De hoogste score is: {} op {} behaald door {}'.format(count, datum, naam))


print(hoogsteScore())