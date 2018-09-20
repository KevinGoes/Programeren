def new_Password(oldPassword, newPassword):
    return newPassword != oldPassword and len(newPassword) >= 6

oldPassword = input("Oude Password: ")
newPassword = input("Nieuwe Password: ")

x = new_Password(oldPassword, newPassword)

print(x)

