def calculate_grade(line):

    line = line[:-1]  

    data = line.split(",")

    name = data[0]

    grade1 = int(data[1])

    grade2 = int(data[2])

    grade3 = int(data[3])

    final_grade = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    if final_grade >= 90:
        letter_grade = "AA"

    elif final_grade >= 85:
        letter_grade = "BA"

    elif final_grade >= 80:
        letter_grade = "BB"

    elif final_grade >= 75:
        letter_grade = "BC"

    elif final_grade >= 70:
        letter_grade = "CC"

    elif final_grade >= 65:
        letter_grade = "DC"

    elif final_grade >= 60:
        letter_grade = "DD"

    elif final_grade >= 55:
        letter_grade = "FD"

    else:
        letter_grade = "FF"

    return name + "------->" + letter_grade + "\n"


with open("direction/grades.txt", "r", encoding="utf-8") as file:

    entries_to_add = []

    for i in file:
        entries_to_add.append(calculate_grade(i))

    with open("direction/final_grades.txt", "w", encoding="utf-8") as file2:

        for i in entries_to_add:
            file2.write(i)
