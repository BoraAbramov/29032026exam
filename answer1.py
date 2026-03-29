















grades = list()
_grade_in = None

while True:
    try:
        _grade_in = int(input("Enter grade: "))
    except ValueError:
        print("Invalid input")
        continue
    if _grade_in == -999:
        if len(grades) < 10:
            print("not enough grades")
            continue
        else:
            break
    grades.append(_grade_in)
    if 0 < _grade_in < 100:
        grades.append(_grade_in)
    else:
        print("Invalid grade")
        continue


