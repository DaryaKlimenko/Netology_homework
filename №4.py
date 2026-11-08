class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if 1 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
                return None
        return 'Ошибка'

    def get_avg_grade(self):
        if not self.grades:
            return 0.0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между студентами"
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между студентами"
        return self.get_avg_grade() > other.get_avg_grade()

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет"

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_avg_grade()}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        if not self.grades:
            return 0.0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между лекторами"
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между лекторами"
        return self.get_avg_grade() > other.get_avg_grade()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.get_avg_grade()}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")



def avg_grades_for_course_students(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])

    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


def avg_grades_for_course_lecturers(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])

    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


student_1 = Student('Дмитрий', 'Казанцев', 'М')
student_2 = Student('Ольга', 'Алёхина', 'Ж')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Пётр', 'Сидоров')

reviewer_1 = Reviewer('Анжела', 'Митрофанова')
reviewer_2 = Reviewer('Алексей', 'Петров')


student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2.courses_in_progress += ['Python']

lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']


student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Git', 9)
student_2.rate_lecture(lecturer_1, 'Python', 8)

student_2.rate_lecture(lecturer_2, 'Python', 9)


reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)


print(" Проверяющий 1 ")
print(reviewer_1)
print("\n Лектор 1 ")
print(lecturer_1)
print("\n Студент 1 ")
print(student_1)

print(f"\nСтудент 1 хуже Студента 2? (по среднему ДЗ): {student_1 < student_2}")
print(f"Лектор 1 лучше Лектора 2? (по средним лекциям): {lecturer_1 > lecturer_2}")

students_all = [student_1, student_2]
lecturers_all = [lecturer_1, lecturer_2]

avg_stud_python = avg_grades_for_course_students(students_all, 'Python')
print(f"Средняя оценка студентов за ДЗ по курсу 'Python': {avg_stud_python}")

avg_lect_python = avg_grades_for_course_lecturers(lecturers_all, 'Python')
print(f"Средняя оценка лекторов за лекции по курсу 'Python': {avg_lect_python}")
