def gemiddeldPerStudent(studentencijfers):
    studentLijst = []
    for i in range(len(studentencijfers)):
        studentLijst.append(round(sum(studentencijfers[i]) / 3, 2))
    return studentLijst


def gemiddeldeVanAlleStudenten(studentencijfers):
    studentLijst = []
    for i in range(len(studentencijfers)):
        studentLijst.append(sum(studentencijfers[i]))
    return round(sum(studentLijst) / 12, 2)


studentencijfers = [ [95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0] ]
print(gemiddeldPerStudent(studentencijfers))
print(gemiddeldeVanAlleStudenten(studentencijfers))