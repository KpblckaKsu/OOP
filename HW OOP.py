class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # оценки

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades_lecturers:  # если курс есть в словаре оценки лектора, то
                lecturer.grades_lecturers[course] += [grade]  # добавляем оценку по ключу Название курса
            else:  # если названия курса нет в словаре, то,
                lecturer.grades_lecturers[course] = [grade]  # создаем новый ключ - Название курса
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        average_grades = round(sum(all_grades) / len(all_grades), 2)
        return average_grades

    def __str__(self):
        date_students = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()} ' \
                        f'\nКурсы в процессе изучения:{",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return date_students

def average_grade_students():
    name_course = 'Python'
    all_students = [sergey, olga]
    all_grades = []
    for student in all_students:
        for course, grade in student.grades.items():
            if course in name_course:
                all_grades.extend(grade)
    return print(f'Средняя оценка за домашние задания по всем студентам: {round(sum(all_grades)/len(all_grades))}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = {}  # прикрепленные курсы


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturers = {}  # оценки
        #self.sr = self.average_grade()

    def average_grade(self):
        all_grades = []
        for grades in self.grades_lecturers.values():
            all_grades += grades
        average_grades = round(sum(all_grades) / len(all_grades), 2)
        return average_grades

    def __str__(self):
        date_lecturer = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'
        return date_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:  # если курс есть в словаре оценки студента, то
                student.grades[course] += [grade]  # добавляем оценку по ключу Название курса
            else:  # если названия курса нет в словаре, то,
                student.grades[course] = [grade]  # создаем новый ключ - Название курса
        else:
            return 'Ошибка'

    def __str__(self):
        date_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return date_reviewer

def average_grade_lecturer():
    name_course = 'Python'
    all_lecturers = [semenov, ivanov]
    all_grades = []
    for lecturer in all_lecturers:
        for course, grade in lecturer.grades_lecturers.items():
            if course in name_course:
                all_grades.extend(grade)
    return print(f'Средняя оценка за лекции всех лекторов: {round(sum(all_grades)/len(all_grades))}')

sergey = Student('Sergey', 'Ivanov')
sergey.courses_in_progress += ['Python']
sergey.finished_courses += ['Git']
olga = Student('Olga', 'Pirogova')
olga.courses_in_progress += ['Python']
olga.finished_courses += ['Git']

petrov = Reviewer('Ivan', 'Petrov')
petrov.courses_attached += ['Python']

petrov.rate_student(sergey, 'Python', 10)
petrov.rate_student(sergey, 'Python', 8)
petrov.rate_student(sergey, 'Python', 7)
petrov.rate_student(olga, 'Python', 9)
petrov.rate_student(olga, 'Python', 9)
petrov.rate_student(olga, 'Python', 8)

semenov = Lecturer('Victor', 'Semenov')
ivanov = Lecturer('Peter', 'Ivanov')
semenov.courses_attached = ['Git', 'Python']
ivanov.courses_attached = ['Git', 'Python', 'JS']
sergey.rate_lecture(semenov, 'Git', 9)
sergey.rate_lecture(semenov, 'Python', 5)
sergey.rate_lecture(semenov, 'Git', 6)
sergey.rate_lecture(ivanov, 'Git', 9)
sergey.rate_lecture(ivanov, 'Python', 7)
sergey.rate_lecture(ivanov, 'Git', 8)

print(sergey.grades)
print(semenov.grades_lecturers)
print(petrov)
print(semenov)
print(sergey)
print(olga)
print(ivanov)
print(ivanov.average_grade())
print(semenov.__lt__(ivanov))

average_grade_students()
average_grade_lecturer()