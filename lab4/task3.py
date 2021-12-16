from pentagon import *
from abc import ABC, abstractclassmethod, abstractmethod

class ICourse(ABC):
    @abstractmethod
    def TakeData(self, id):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Course(ICourse):
    def __init__(self):
        self.CourseName = None
        self.program = None
        self.place = None

    def TakeData(self, id, teacher1):
        try:
            # sqlQuery = "SELECT CourseTeacherID FROM course WHERE CourseTeacherID = '{0}'"
            # MyCursor.execute(sqlQuery.format(str(id)))
            # MyResult = MyCursor.fetchone()[0]
            self.CourseName = teacher1
            sqlQuery = "SELECT CourseProgram FROM course WHERE CourseTeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(id)))
            MyResult = MyCursor.fetchone()[0]
            self.program = MyResult
            sqlQuery = "SELECT CoursePlace FROM course WHERE CourseTeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(id)))
            MyResult = MyCursor.fetchone()[0]
            self.place = MyResult
        except Exception as error:
            print("Failed to info from the table", error)

    def __str__(self):
        return f"Yo selected Course\n" \
               f"{self.CourseName}\n" \
               f"Program: {self.program}\n" \
               f"Place: {self.place}\n"

class ILocalCourse(Course):
    pass

class IOfficeCourse(Course):
    pass

class ITeacher(ABC):
    @abstractmethod
    def TakeData(self, id):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Teacher(ITeacher):
    def __init__(self, id):
        self.name = None
        self.course = None
        self.id = id

    def TakeData(self):
        try:
            sqlQuery = "SELECT TeacherName FROM teacher WHERE TeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.name = MyResult
            sqlQuery = "SELECT TeacherSurname FROM teacher WHERE TeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.name += " " + MyResult
            sqlQuery = "SELECT TeacherCourse FROM teacher WHERE TeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.course = MyResult
        except Exception as error:
            print("Failed to info from the table", error)

    def __str__(self):
        return f"Teacher Full name: {self.name}\n" \
               f"Course: {self.course}"



class ICourseFactory(ABC):
    @abstractmethod
    def withdrawCourse(self):
        print("withdraw info about selected course")



class CourseFactory():
    def __init__(self, choice):
        self.choice = choice

    def withdrawCourse(self):
        teacher1 = Teacher(self.choice)
        teacher1.TakeData()

        course = Course()
        course.TakeData(self.choice, teacher1)
        print(course)

def main():


    print("1 - SpeedRaceCourse")
    print("2 - HikingClub")
    print("3 - BoringCourse")
    choice = input("select: ")
    factory = CourseFactory(choice)
    factory.withdrawCourse()


main()
