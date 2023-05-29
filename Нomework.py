class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def av_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.av_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории не сравниваем.")
            return
        return self.av_rate() < other.av_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rate(self):
        sum_r = 0
        len_r = 0
        for mark in self.grades.values():
            sum_r += sum(mark)
            len_r += len(mark)
        res = round(sum_r / len_r, 2)
        return res

    def av_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rate()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Разные категории между собой не сравниваем!')
            return
        return self.av_rate() < other.av_rate()


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
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Студенты
student_1 = Student('Иван', 'Иванов', 'Он')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Юлия', 'Петрова', 'Она')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

student_3 = Student('Максим', 'Максимов', 'Он')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer_1 = Lecturer('Ольга', 'Ивановна')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Иван', 'Олегович')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Светлана', 'Сергеева')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Тимур', 'Тимуров')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 6)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rate_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
