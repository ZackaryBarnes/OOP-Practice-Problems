class Student:

    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        else:
            self._grade = grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        total_grades = 0
        for student in students:
            total_grades += student.grade

        average_grade = total_grades / len(students)
        return average_grade

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1

        current_total = 0 
        for student in cls.all_students:
            current_total += student.grade

        average_grade = current_total / len(cls.all_students)    
        return average_grade
    
    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None
        
        best_student = None
        for student in cls.all_students:
            if best_student == None or student.grade > best_student.grade:
                best_student = student
        return best_student