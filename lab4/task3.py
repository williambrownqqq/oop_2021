# """ main module of program """
#
# from pentagon import *
# from abc import ABC, abstractclassmethod, abstractmethod
#
# class ICourse(ABC):
#     """Abstract class for 'Courses' """
#
#     """ take data for course from database """
#     @abstractmethod
#     def TakeData(self, teacher):
#         pass
#
#     """withdraw info """
#     @abstractmethod
#     def __str__(self):
#         pass
#
#
# class Course(ICourse):
#     """ Create common course """
#
#     def __init__(self, id):
#         self.CourseName = None
#         self.program = None
#         self.place = None
#         self.id = id
#
#     """ take data for course from database """
#     def TakeData(self, teacher1):
#         try:
#             print("id = ", self.id)
#             self.CourseName = teacher1
#             sqlQuery = f"SELECT CourseProgram FROM course WHERE CourseTeacherID = {self.id}"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.program = MyResult
#             sqlQuery = f"SELECT CoursePlace FROM course WHERE CourseTeacherID = {self.id}"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.place = MyResult
#         except Exception as error:
#             print("1Failed to take info from the table", error)
#
#     # def __str__(self):
#     #     return f"Yo selected Course\n" \
#     #            f"{self.CourseName}\n" \
#     #            f"Program: {self.program}\n" \
#     #            f"Place: {self.place}\n"
#
#
# class ILocalCourse(Course):
#     """ Create Local course """
#     def __init__(self, id):
#         super().__init__(id)
#         self.CourseType = None
#
#     """ method for define location"""
#     def localisation(self):
#         try:
#             sqlQuery = "SELECT Localisation FROM course WHERE CourseTeacherID = '{0}'"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.CourseType = MyResult
#
#         except Exception as error:
#             print("Failed to take info from the table", error)
#
#     def __str__(self):
#         return f"Yo selected Course\n" \
#                f"{self.CourseName}\n" \
#                f"Program: {self.program}\n" \
#                f"Place: {self.place}\n" \
#                f"Type: {self.CourseType}\n"
#
#
# class IOfficeCourse(Course):
#     """ Create Local course """
#     def __init__(self, id):
#         super().__init__(id)
#         self.CourseType = None
#
#     """ method for define location"""
#     def localisation(self):
#         try:
#             sqlQuery = "SELECT Localisation FROM course WHERE CourseTeacherID = '{0}'"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.CourseType = MyResult
#
#         except Exception as error:
#             print("Failed to info from the table", error)
#
#     def __str__(self):
#         return f"Yo selected Course\n" \
#                f"{self.CourseName}\n" \
#                f"Program: {self.program}\n" \
#                f"Place: {self.place}\n" \
#                f"Type: {self.CourseType}\n"
#
#
#
# class ITeacher(ABC):
#     """Abstract class for 'Teacher' """
#
#     @abstractmethod
#     def TakeData(self):
#         pass
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#
# class Teacher(ITeacher):
#     def __init__(self, id):
#         self.name = None
#         self.course = None
#         self.id = id
#
#     def TakeData(self):
#         try:
#             sqlQuery = "SELECT TeacherName FROM teacher WHERE TeacherID = '{0}'"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.name = MyResult
#             sqlQuery = "SELECT TeacherSurname FROM teacher WHERE TeacherID = '{0}'"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.name += " " + MyResult
#             sqlQuery = "SELECT TeacherCourse FROM teacher WHERE TeacherID = '{0}'"
#             MyCursor.execute(sqlQuery.format(str(self.id)))
#             MyResult = MyCursor.fetchone()[0]
#             self.course = MyResult
#         except Exception as error:
#             print("Failed to take info from the table", error)
#
#     def __str__(self):
#         return f"Course: {self.course}\n" \
#                f"Teacher Full name: {self.name}"
#
# """Abstract class for 'CourseFactory' """
# class ICourseFactory(ABC):
#     @abstractmethod
#     def withdrawCourse(self):
#         print("withdraw info about selected course")
#
# """ Create course and teacher for chosen course"""
# class CourseFactory():
#     def __init__(self, choice, local):
#         self.choice = choice
#         self.local = local
#
#     """ Create course and teacher """
#     def withdrawCourse(self):
#         if self.local == "local":
#             teacher1 = Teacher(self.choice)
#             teacher1.TakeData()
#
#             course = ILocalCourse(self.choice)
#             course.TakeData(teacher1)
#             course.localisation()
#             print(course)
#
#         elif (self.local == "office"):
#             teacher1 = Teacher(self.choice)
#             teacher1.TakeData()
#
#             course = IOfficeCourse(self.choice)
#             course.TakeData(teacher1)
#             course.localisation()
#             print(course)
#
#
# def main():
#     print("local/office")
#     while True:
#         local = input("select: ")
#         if local.lower() in ['local', 'office']:
#             break
#         else:
#             print(f"wrong choice, try again")
#
#     if local == "local":
#         print("1 - SpeedRaceCourse")
#         print("2 - HikingClub")
#         print("3 - DirtJumpingCourse")
#     elif local == "office":
#         print("4 - BoringCourse")
#         print("5 - C# course")
#         print("6 - Python course")
#
#     while True:
#         choice = input("select: ")
#         if int(choice) in range(4, 7) and local == "office":
#             break
#         if int(choice) in range(1, 4) and local == "local":
#             break
#         else:
#             print(f"wrong choice, try again")
#
#     if (local == "local" and int(choice) in range(1, 4)) or (local == "office" and int(choice) in range(4, 7)):
#         factory = CourseFactory(choice, local)
#         factory.withdrawCourse()
#     else:
#         print("wrong choice")
#
#
# main()

""" main module of program """

from pentagon import *
from abc import ABC, abstractclassmethod, abstractmethod

class ITeacher(ABC):
    """Abstract class for 'Teacher' """

    @abstractmethod
    def TakeData(self):
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
            print("Failed to take info from the table", error)

    def __str__(self):
        return f"Course: {self.course}\n" \
               f"Teacher Full name: {self.name}"

class ICourse(ABC):
    """Abstract class for 'Courses' """

    """ take data for course from database """
    @abstractmethod
    def TakeData(self, teacher):
        pass

    """withdraw info """
    @abstractmethod
    def __str__(self):
        pass

class Course(ICourse):
    """ Create common course """

    def __init__(self, id):
        self.CourseName = None
        self.program = None
        self.place = None
        self.id = id

    """ take data for course from database """
    def TakeData(self, teacher1):
        try:
            print("id = ", self.id)
            self.CourseName = teacher1
            sqlQuery = f"SELECT CourseProgram FROM course WHERE CourseTeacherID = {self.id}"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.program = MyResult
            sqlQuery = f"SELECT CoursePlace FROM course WHERE CourseTeacherID = {self.id}"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.place = MyResult
        except Exception as error:
            print("1Failed to take info from the table", error)

    # def __str__(self):
    #     return f"Yo selected Course\n" \
    #            f"{self.CourseName}\n" \
    #            f"Program: {self.program}\n" \
    #            f"Place: {self.place}\n"

class ILocalCourse(ABC):

    @abstractmethod
    def localisation(self): pass

    @abstractmethod
    def __str__(self): pass

class IOffsiteCourse(ABC):

    @abstractmethod
    def localisation(self): pass

    @abstractmethod
    def __str__(self): pass

class LocalCourse(Course):
    """ Create Local course """
    def __init__(self, id):
        super().__init__(id)
        self.CourseType = None

    """ method for define location"""
    def localisation(self):
        try:
            sqlQuery = "SELECT Localisation FROM course WHERE CourseTeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.CourseType = MyResult

        except Exception as error:
            print("Failed to take info from the table", error)

    def __str__(self):
        return f"Yo selected Course\n" \
               f"{self.CourseName}\n" \
               f"Program: {self.program}\n" \
               f"Place: {self.place}\n" \
               f"Type: {self.CourseType}\n"

class OfficeCourse(Course):
    """ Create Local course """
    def __init__(self, id):
        super().__init__(id)
        self.CourseType = None

    """ method for define location"""
    def localisation(self):
        try:
            sqlQuery = "SELECT Localisation FROM course WHERE CourseTeacherID = '{0}'"
            MyCursor.execute(sqlQuery.format(str(self.id)))
            MyResult = MyCursor.fetchone()[0]
            self.CourseType = MyResult

        except Exception as error:
            print("Failed to info from the table", error)

    def __str__(self):
        return f"Yo selected Course\n" \
               f"{self.CourseName}\n" \
               f"Program: {self.program}\n" \
               f"Place: {self.place}\n" \
               f"Type: {self.CourseType}\n"



"""Abstract class for 'CourseFactory' """
class ICourseFactory(ABC):
    @abstractmethod
    def withdrawCourse(self):
        print("withdraw info about selected course")

    @abstractmethod
    def teacher_factory(self):
        pass

""" Create course and teacher for chosen course"""
class CourseFactory():
    def __init__(self, choice, local):
        self.choice = choice
        self.local = local

    """ Create course and teacher """
    def withdrawCourse(self):
        if self.local == "local":
            teacher1 = Teacher(self.choice)
            teacher1.TakeData()

            course = LocalCourse(self.choice)
            course.TakeData(teacher1)
            course.localisation()
            print(course)

        elif (self.local == "office"):
            teacher1 = Teacher(self.choice)
            teacher1.TakeData()

            course = OfficeCourse(self.choice)
            course.TakeData(teacher1)
            course.localisation()
            print(course)


def main():
    print("local/office")
    while True:
        local = input("select: ")
        if local.lower() in ['local', 'office']:
            break
        else:
            print(f"wrong choice, try again")

    if local == "local":
        print("1 - SpeedRaceCourse")
        print("2 - HikingClub")
        print("3 - DirtJumpingCourse")
    elif local == "office":
        print("4 - BoringCourse")
        print("5 - C# course")
        print("6 - Python course")

    while True:
        choice = input("select: ")
        if int(choice) in range(4, 7) and local == "office":
            break
        if int(choice) in range(1, 4) and local == "local":
            break
        else:
            print(f"wrong choice, try again")

    if (local == "local" and int(choice) in range(1, 4)) or (local == "office" and int(choice) in range(4, 7)):
        factory = CourseFactory(choice, local)
        factory.withdrawCourse()
    else:
        print("wrong choice")


main()
