
def grade_collect(grades) -> list:
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
                return grades
        if 0 < _grade_in < 100:
            grades.append(_grade_in)
        else:
            print("Invalid grade")
            continue

def calculate(grade_collect, grades) -> list:
    _count = 0
    for grade in grades:
        _count += grade
    _avg = _count / len(grades)

    _max = max(grades)

    return f"The average {_avg}, The max grade {_max}"


grades = list()

grade_collect(grades)
_stat_fun = calculate(grade_collect, grades)
print(_stat_fun)
print(grades)





