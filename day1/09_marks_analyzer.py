def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def show_report(students):
    all_marks = list(students.values())

    total = sum(all_marks)
    average = total / len(all_marks)
    highest = max(all_marks)
    lowest = min(all_marks)

    print("===== MARKS REPORT =====")
    for name in students:
        marks = students[name]
        if marks >= 50:
            result = "Pass"
        else:
            result = "Fail"
        print(name, "-", marks, "-", get_grade(marks), "-", result)

    print("------------------------")
    print("Total marks :", total)
    print("Average     :", round(average, 2))

    for name in students:
        if students[name] == highest:
            print("Highest     :", highest, "(" + name + ")")
        if students[name] == lowest:
            print("Lowest      :", lowest, "(" + name + ")")

    pass_count = 0
    for m in all_marks:
        if m >= 50:
            pass_count += 1
    print("Passed      :", pass_count, "out of", len(all_marks))


class_marks = {
    "Ali": 78,
    "Sara": 92,
    "Ahmed": 55,
    "Fatima": 88,
    "Usman": 41,
    "Zainab": 67,
}

show_report(class_marks)
