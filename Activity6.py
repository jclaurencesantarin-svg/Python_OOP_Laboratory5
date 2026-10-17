class Student:
    def __init__(self):
        self.__grade = 0

    def study(self):
        print("Student is studying.")

class CollegeStudent(Student):
    def study(self):
        print("College student is studying programming.")

if __name__ == "__main__":
    regular_student = Student()
    college_student = CollegeStudent()

    regular_student.study()
    college_student.study()