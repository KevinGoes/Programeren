def lijst(file):
    infile = open(file, "r")
    invoer = infile.readlines()
    infile.close()
    for i in invoer:
        i.split(",")
        print(i[8:-1], "heeft kaartnummer:",i[:6])


file = "kaartnummers.txt"
lijst(file)
