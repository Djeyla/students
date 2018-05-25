students = [
    {"name": "Джон", "surname": "Леннон", "gender": "мужской", "experience": "true", "homework": [7, 6, 10, 8, 5],
     "exam": 9, },

    {"name": "Пол", "surname": "Маккартни", "gender": "мужской", "experience": "false", "homework": [6, 6, 5, 7, 6],
     "exam": 7, },

    {"name": "Эми", "surname": "Уайнхаус", "gender": "женский", "experience": "true", "homework": [6, 7, 4, 7, 5],
     "exam": 5, },

    {"name": "Курт", "surname": "Кобейн", "gender": "мужской", "experience": "false", "homework": [4, 4, 4, 6, 3],
     "exam": 4, },

    {"name": "Кристина", "surname": "Агилера", "gender": "женский", "experience": "true", "homework": [7, 10, 10, 8, 7],
     "exam": 9, },

    {"name": "Элла", "surname": "Фицджеральд", "gender": "женский", "experience": "false", "homework": [6, 7, 9, 8, 7],
     "exam": 8, }
]

students_man = 0
students_woman = 0
students_with_exp = 0
students_without_exp = 0
avrg_hmv = 0
avrg_exam = 0
avrg_hmw_man = 0
avrg_exam_man = 0
avrg_hmw_woman = 0
avrg_exam_woman = 0
avrg_hmw_students_with_exp = 0
avrg_exam_students_with_exp = 0
avrg_hmw_students_without_exp = 0
avrg_exam_students_without_exp = 0
res_integr_grade = []
best_students = []


# format(x, '0.2f')
def main(a, b, c, d):
    for students_grades in students:
        a += sum(students_grades['homework']) / len(students_grades['homework'])
        b += students_grades['exam']
    print(c, format(a / len(students), '0.1f'))
    print(d, format(b / len(students), '0.1f'))


main(avrg_hmv, avrg_exam, 'Средняя оценка за домашние задания по группе: ', 'Средняя оценка за экзамен: ')


def main_if(key, value, e, a, b, c, d):
    for students_grades in students:
        if students_grades[key] == value:
            e += 1
            a += sum(students_grades['homework']) / len(students_grades['homework'])
            b += students_grades['exam']
        else:  # пункт на случай, если группы не окажется
            continue
    print(c, format((a / e), '0.1f'))
    print(d, format((b / e), '0.1f'))


def best_grades():
    for students_grades in students:
        x = 0.6 * sum(students_grades['homework']) / len(students_grades['homework']) + 0.4 * students_grades['exam']
        students_grades.setdefault('integr_grade', x)
        res_integr_grade.append(students_grades['integr_grade'])


def best_of_the_best_student():
    for students_grades in students:
        if students_grades['integr_grade'] == max(res_integr_grade):
            best_students.append(students_grades['name'])
            if len(best_students) > 1:
                print('Лучшие студенты:', best_students)
                return
            else:
                print('Лучший студент:', best_students)


main_if('gender', 'мужской', students_man, avrg_hmw_man, avrg_exam_man, 'Средняя оценка за домашние задания у мужчин: ',
        'Средняя оценка за экзамен у мужчин: ')

main_if('gender', 'женский', students_woman, avrg_hmw_woman, avrg_exam_woman,
        'Средняя оценка за домашние задания у женщин: ', 'Средняя оценка за экзамен у женщин: ')

main_if('experience', 'true', students_with_exp, avrg_hmw_students_with_exp, avrg_exam_students_with_exp,
        'Средняя оценка за домашние задания у студентов с опытом: ', 'Средняя оценка за экзамен у студентов с опытом: ')

main_if('experience', 'false', students_without_exp, avrg_hmw_students_without_exp, avrg_exam_students_without_exp,
        'Средняя оценка за домашние задания у студентов без опыта: ',
        'Средняя оценка за экзамен у студентов без опыта: ')

best_grades()
best_of_the_best_student()