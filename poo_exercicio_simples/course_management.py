class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, enrollment):
        super().__init__(name, age)
        self.enrollment = enrollment #matricula
        self.enrolled_courses = []

    def add_course(self, course):
        self.enrolled_courses.append(course)

    def __str__(self):
        if not self.enrolled_courses:
            return f"{self.name} ({self.enrollment}) - is not enrolled in any course"
        
        else:
            return f"Student: {self.name} (Enrollment: {self.enrollment}, Age: {self.age})"
        
class Course:
    def __init__(self, name, workload):
        self.name = name
        self.workload = workload #carga horaria dp curso
        self.course_instructor = None #Professor responsavel
        self.students = []

    def add_student(self, students):
        self.students.append(students)

class Teacher(Person):
        def __init__(self, name, age, field):
            super().__init__(name, age)
            self.field = field#area que atua no professor

class School:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def list_courses(self):
        for course in self.courses:
            print(f"\nCourse: {course.name}")
            print(f"Instructor: {course.course_instructor.name}")

            if not course.students:
                print("no students enrolled")
            else:
                print("Student Enrolled")
                for student in course.students:
                    if not student.enrolled_courses:
                        print(f"{student.name} - (no enrolled courses)")
                    else:
                        course_names = ", ".join(c.name for c in student.enrolled_courses)
                        print(f"{student.name} - {course_names}")

#Creating instances of the class "Student" 🧑‍🎓
student1 = Student('João Paulo', 40, 'S0001')
student2 = Student('Ana Medeiros', 33, 'S0002')
student3 = Student('Jenyfer Muller', 34, 'S0003')
student4 = Student('Astrogildo Silva', 38, 'S0004')

#Creating instances of the class "Course" 📚
course1 = Course('Python', 350)
course2 = Course('Java', 300)
course3 = Course('mySQL', 250)
course4 = Course('C++', 500)
course5 = Course('Redes de computadores', 280)

#Creating instances of the class "Teacher" 👩‍🏫
teacher1 = Teacher('Gustavo Guanabara', 47, 'Programação e analise de dados')
teacher2 = Teacher('Fernando Costa', 53, 'Programação')
teacher3 = Teacher('Mariana dadecosta', 21, 'Informática')
teacher4 = Teacher('Juberaldo da Silva', 85, 'Programação')

#Creating instances of the class "Scholl" 🏫
tec_school = School('Technology of School')

#Association between course and teacher
course1.course_instructor = teacher1
course2.course_instructor = teacher4
course3.course_instructor = teacher1
course4.course_instructor = teacher2
course5.course_instructor = teacher3

# Bidirectional aggregation: add the student to the course and the course to the student's list
course1.add_student(student1)
student1.add_course(course1)

course2.add_student(student2)
student2.add_course(course2)

course3.add_student(student3)
student3.add_course(course3)

course4.add_student(student4)
student4.add_course(course4)

#Adding teachers to the School class teachers list
tec_school.add_teacher(teacher1)
tec_school.add_teacher(teacher2)
tec_school.add_teacher(teacher3)
tec_school.add_teacher(teacher4)

#Adding courses to the School class courses list
tec_school.add_course(course1)
tec_school.add_course(course2)
tec_school.add_course(course3)
tec_school.add_course(course4)
tec_school.add_course(course5)

# Display all courses offered by the school along with instructors and enrolled students
tec_school.list_courses()