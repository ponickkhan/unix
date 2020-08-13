# Name : Md.Rafiuzzaman Khan
# ID   : 011161017

# Students Result Data
student_info = {
    "Md. Hasan": 92,
    "Mehrub Hossain": 20,
    "Md.Rafiuzzaman Khan": 81,
    "Samiul Ahmed": 67,
    "Pranto Shikdar": 56,
    "Nusrat Jahan": 38,
    "Hasibul Haque": 75,
    "Abir Hasan": 66,
    "Tamanna Afroz": 30,
    "Mobassher Billah": 78
}


def result_insight(student_info):
    minimum = [key for key in student_info if
               all(student_info[temp] >= student_info[key]
                   for temp in student_info)]

    maximum = [key for key in student_info if
               all(student_info[temp] <= student_info[key]
                   for temp in student_info)]

    # printing result
    print("Highest Mark:", maximum[0], "(", student_info.get(maximum[0]), ")")
    print("Lowest Mark:", minimum[0], "(", student_info.get(minimum[0]), ")")

    lp = 0  # counter for marks bellow 40
    hp = 0  # counter for marks above 80
    for key in student_info:
        if student_info[key] > 80:
            hp = hp + 1  # students that achieved 80 or more
        if student_info[key] < 40:
            lp = lp + 1  # students that failed

    print('{}%'.format(int(round((hp / len(student_info) * 100)))), "students achieved 80 or more")
    print('{}%'.format(int(round((lp / len(student_info) * 100)))), "students are failed")


print("Output:")
result_insight(student_info)
