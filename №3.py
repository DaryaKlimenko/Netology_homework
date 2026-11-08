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
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')


student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python']


student.rate_lecture(lecturer, 'Python', 10)
student.rate_lecture(lecturer, 'Python', 9)


reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 8)


print(reviewer, "\n")
print(lecturer, "\n")
print(student)