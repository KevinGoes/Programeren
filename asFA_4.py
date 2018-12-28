import random


def my_sort(lst):
    if len(lst) <= 1:                                   # Er is nu niks meer te sorteren
        return lst

    midden = int(len(lst) / 2)                          # Int omdat je anders een komma getal krijgt
    links = my_sort(lst[:midden])                       # Recurie met linker helft van de lijst
    rechts = my_sort(lst[midden:])                      # Recursie met rechter helft van de lijst

    i = 0                                               # Teller op 0 zetten

    while len(links) != 0 and len(rechts) != 0:         # Zolang er nog items in de links en rechts zitten
        if links[0] < rechts[0]:                        # Eerste item van links is kleiner dan eerste item van rechts
            tmp = links[0]                              # Opslaan van eerste item van links
            links.pop(0)                                # Verwijderen van eerste item van links3
            lst[i] = tmp                                # Bij lijst wordt het opgeslagen item geplaatst

        else:                                           # Eerste item van links is groter dan eerste item van rechts
            tmp = rechts[0]                             # Opslaan van eerste item van rechts
            rechts.pop(0)                               # Verwijderen van eerste item van rechts
            lst[i] = tmp                                # Bij lijst wordt het opgeslagen item geplaatst

        i += 1                                          # Teller wordt met 1 verhoogd

    return lst[:-len(links + rechts)] + links + rechts


def random_lst():
    lst = []
    i = random.randint(1, 99)                           # Random lengte van de lijst
    while i != 0:                                       # Zolang de lengte nog niet 0 is
        lst.append(random.randint(1, 99))               # Random getal toevoegen aan lijst
        i -= 1                                          # Lengte verminderen met 1
    return lst


def random_lst_no_duplicate():
    lst = []
    i = random.randint(5, 25)
    while i != 0:
        newInt = random.randint(1, 99)
        if newInt not in lst:
            lst.append(newInt)
        i -= 1
    return lst


def check_sort(lst):
    if len(lst) <= 1:
        return True

    else:
        return lst[0] < lst[1] and check_sort(lst[1:-1])


# i = 10
# while i != 0:
#     tmpLst = random_lst_no_duplicate()
#     print('{} \n Check = {} \n\n'.format(my_sort(tmpLst),check_sort(my_sort(tmpLst))))
#     i -= 1

print(my_sort([5, 13, 42, 11, 9]))