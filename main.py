class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_value(self):
        aver_lect = 0
        count = 0
        for average in self.grades.values():
            for aver in average:
                aver_lect += aver
                count += 1
        average_grade = aver_lect / count
        return average_grade

    def __str__(self):
        lectname = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_value()}'
        return lectname

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.aver_value() < other.aver_value()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_students(self):
        aver_lect = 0
        count = 0
        for average in self.grades.values():
            for aver in average:
                aver_lect += aver
                count += 1
        average_grade = aver_lect / count
        return average_grade

    def __str__(self):
        lectname = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_students()}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return lectname

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_students() < other.average_students()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__ (self):
        revname = f'Имя: {self.name}\nФамилия: {self.surname}'
        return revname




cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor_other = Mentor('Coll', 'Bobs')
cool_mentor_other.courses_attached += ['Python']

cool_lecturer = Lecturer('Egor', 'Grech')
cool_lecturer.courses_attached +=['Python']

cool_lecturer_other = Lecturer('Arslan', 'Dzagoev')
cool_lecturer_other.courses_attached +=['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

not_bad_student = Student('Sanya', 'Kokov', 'your_gender')
not_bad_student.courses_in_progress += ['Python']
not_bad_student.finished_courses += ['Введение в программирование']
not_bad_student.rate_lecturer(cool_lecturer, 'Python', 9)

best_student_other = Student('Rayaan', 'Amenbek', 'your_gender')
best_student_other.courses_in_progress += ['Git']
best_student_other.finished_courses += ['Введение в программирование']
best_student_other.rate_lecturer(cool_lecturer_other, 'Git', 8)

cool_reviewer = Reviewer('Amir', 'Dautov')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(not_bad_student, 'Python', 9)

cool_reviewer_other = Reviewer('Ino', 'Agent')
cool_reviewer_other.courses_attached += ['Git']
cool_reviewer_other.rate_hw(best_student_other, 'Git', 8)

list_students = [best_student, not_bad_student, best_student_other]
list_lectur = [cool_lecturer, cool_lecturer_other]

def average_students_courses(list_st, name_courses):
    aver_dz = 0
    count = 0
    for ls in list_st:
        for ls_courses in ls.grades.keys():
            if name_courses == ls_courses:
                for not_ls in ls.grades[name_courses]:
                    aver_dz += not_ls
                    count += 1
                    average_grade = aver_dz / count
    return average_grade

def average_lecturer_courses(list_lect, name_courses):
    aver_dz = 0
    count = 0
    for ls in list_lect:
        for ls_courses in ls.grades.keys():
            if name_courses == ls_courses:
                for not_ls in ls.grades[name_courses]:
                    aver_dz += not_ls
                    count += 1
                    average_grade = aver_dz / count
    return average_grade

print(average_students_courses(list_students, 'Git'))
print(average_lecturer_courses(list_lectur, 'Python'))

print(cool_lecturer.aver_value())
print(cool_lecturer.grades)
print(cool_lecturer_other.aver_value())
print(cool_lecturer_other.grades)
print(best_student)
print(cool_lecturer)
print(cool_reviewer)
print(cool_lecturer_other < cool_lecturer)
print(best_student > best_student_other)


