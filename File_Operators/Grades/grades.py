def calculate_grade(name, final_score):

    if final_score >= 55:
        with open("file_address/passed.txt", "a", encoding="utf-8") as file:

            if final_score >= 90:
                letter = "AA"
            elif final_score >= 85:
                letter = "BA"
            elif final_score >= 80:
                letter = "BB"
            elif final_score >= 75:
                letter = "BC"
            elif final_score >= 70:
                letter = "CC"
            elif final_score >= 65:
                letter = "DC"
            elif final_score >= 60:
                letter = "DD"


            file.write(name + "----->" + letter + "\n")
            return name + "----->" + letter

    else:
        with open("file_address/failed.txt", "a", encoding="utf-8") as file:
            if final_score < 60:
                letter = "FF"
                file.write(name + "----->" + letter + "\n")
                return name + "----->" + letter


name = input("Enter the student's name:")
grades = input("Please enter the student's name followed by their grades, separated by commas:")
grades_list = []
grades_list = grades.split(",")

grade1 = grades_list[0]
grade2 = grades_list[1]
grade3 = grades_list[2]

grade1 = int(grade1)
grade2 = int(grade2)
grade3 = int(grade3)

final_score = grade1 * 3/10 + grade2 * 3/10 + grade3 * 4/10

calculate_grade(name, final_score)
print(calculate_grade(name, final_score))
