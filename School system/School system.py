class Person:
    def __init__(self, f_name, l_name, age, password, m_name):
        self.__f_name = f_name.title()
        self.__l_name = l_name.title()
        self.__m_name = m_name.title()
        self.__age = age
        self.__e_email = (self.__f_name[0] + self.__l_name + "@psu.com").lower()
        self.__password = password

    @staticmethod
    def string_has_number(string):
        return any(char.isdigit() for char in string)

    def get_first_name(self):
        return self.__f_name

    def set_first_name(self, f_name):
        if self.string_has_number(f_name):
            print("The first name has a number")
        else:
            self.__f_name = f_name.title()

    def get_last_name(self):
        return self.__l_name

    def set_last_name(self, l_name):
        if self.string_has_number(l_name):
            print("The last name has a number")
        else:
            self.__l_name = l_name.upper()

    def get_middle_name(self):
        return self.__m_name

    def set_middle_name(self, m_name):
        if self.string_has_number(m_name):
            print("The middle name has a number")
        else:
            self.__m_name = m_name.title()

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_email(self):
        return self.__e_email

    def set_email(self, new_email):
        self.__e_email = new_email

    def get_password(self):
        return self.__password

    def set_password(self):
        old_password = input("Enter your old password ")
        for tries in range(0, 4):
            if old_password != self.__password:
                old_password = input("Wrong password, enter your password again")
            else:
                break
            if tries == 3:
                print("Tries exceeded! Login out!")
                return exit()
        new_password = input("Please enter your password")
        while len(new_password) < 6:
            new_password = input("Password should contain 6 or more characters! Please enter a new password ")
        self.__password = new_password

    def administrator_set_password(self, password):
        while len(password) < 6:
            password = input("Password should contain 6 or more characters! Please enter a new password ")
        self.__password = password


class Student(Person):
    number_of_students = 0

    def __init__(self, f_name, l_name, age, password, grade, speciality, group_number, m_name=""):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade = grade.upper()
        self.__speciality = speciality.upper()
        self.__group_number = group_number
        self.__id = "STD" + "_" + self.__grade[0:3] + "_" + self.__speciality[0:3] + "_" + \
                    str(self.__group_number) + "_" + str(self.number_of_students)
        self.__maths = None
        self.__informatics = None
        self.__electronics = None

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = "STD" + "_" + self.__grade[0:3] + "_" + self.__speciality[0:3] + "_" + \
                    str(self.__group_number) + "_" + str(self.number_of_students)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        while grade.upper() not in ("FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"):
            grade = input("Wrong grade! Please enter the correct grade")
        else:
            self.__grade = grade.upper()
            self.set_id()

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, speciality):
        while speciality.upper() not in ("PYTHON", "JAVA", "PHP"):
            speciality = input("Wrong speciality! Please enter the correct speciality")
        else:
            self.__speciality = speciality.upper()
            self.set_id()

    def get_group_number(self):
        return self.__group_number

    def set_group_number(self, group_number):
        while group_number not in range(1, 30):
            group_number = int(input("Group number out of range! Please enter the correct group"))
        else:
            self.__group_number = group_number
            self.set_id()

    def get_maths(self):
        return self.__maths

    def set_math(self, math):
        if 0 <= math <= 100:
            self.__maths = math
        else:
            return "Out of range"

    def get_informatics(self):
        return self.__informatics

    def set_informatics(self, informatics):
        if 0 <= informatics <= 100:
            self.__maths = informatics
        else:
            return "Out of range"

    def get_electronics(self):
        return self.__electronics

    def set_electronics(self, electronics):
        if 0 <= electronics <= 100:
            self.__maths = electronics
        else:
            return "Out of range"

    def get_average(self):
        if self.__maths and self.__speciality and self.__electronics:
            print(self.get_first_name(), self.get_last_name(), end=": ")
            return round((self.__maths + self.__speciality + self.__electronics) / 3, 2)
        else:
            print("Maths: ", self.__maths)
            print("Speciality: ", self.__speciality)
            print("Electronics: ", self.__electronics)

            return "Student does not have all marks"

    def define(self):
        if self.get_middle_name():
            print("This is student", self.get_first_name(), self.get_last_name(),
                  self.get_middle_name(), "and his ID is: ", self.get_id())
        else:
            print("This is student", self.get_first_name(), self.get_last_name(), "and his ID is: ", self.get_id())


class Professor(Person):
    number_of_professors = 0

    def __init__(self, f_name, l_name, age, password, grade, speciality, teaching_hours, m_name=""):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade = grade
        self.__speciality = speciality.upper()
        self.__teaching_hours = teaching_hours
        self.__id = "PRO" + "_" + str(self.__grade) + "_" + self.__speciality + "_" + str(self.number_of_professors)

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = "PRO" + "_" + str(self.__grade) + "_" + self.__speciality + "_" + str(self.number_of_professors)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        while grade not in range(0, 6):
            grade = int(input("Wrong grade! Please enter a new grade "))
        else:
            self.__grade = grade
            self.set_id()

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, speciality):
        while speciality.upper() not in ("MATH", "ELECTRONICS", "INFORMATICS"):
            speciality = input("Wrong speciality! Please enter a correct speciality!")
        else:
            self.__speciality = speciality.upper()
            self.set_id()

    def get_teaching_hours(self):
        return self.__teaching_hours

    def set_teaching_hours(self, teaching_hours):
        while teaching_hours not in range(5, 26):
            teaching_hours = int(input("Teaching hours out of range! Please enter new teaching hours"))
        self.__teaching_hours = teaching_hours

    def get_salary(self):
        basic_salary = 2000
        print("The salary of the professor is", self.get_first_name(), self.get_last_name(), "is", end=" ")
        salary = str(
            round((basic_salary + (self.get_grade() / 100) * basic_salary + self.__teaching_hours * 20), 2)) + "$"
        return salary

    def define(self):
        if self.get_middle_name():
            print("This is professor", self.get_first_name(), self.get_last_name(),
                  self.get_middle_name(), "and his ID is: ", self.get_id())
        else:
            print("This is professor", self.get_first_name(), self.get_last_name(), "and his ID is: ", self.get_id())


class Administrator(Person):
    number_of_administrators = 0

    def __init__(self, f_name, l_name, age, password, grade, speciality, m_name=""):
        super().__init__(f_name, l_name, age, password, m_name)
        self.__grade = grade
        self.__speciality = speciality.upper()
        self.__id = "ADM" + "_" + str(self.__grade) + "_" + self.__speciality[0:3] + str(self.number_of_administrators)

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = "ADM" + "_" + str(self.__grade) + "_" + self.__speciality[0:3] + str(self.number_of_administrators)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if grade not in range(0, 6):
            print("Wrong grade")
        else:
            self.__grade = grade
            self.set_id()

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, speciality):
        if speciality.upper() not in ("STUDENTS", "PROFESSORS", "ADMINS"):
            print("Wrong speciality")
        else:
            self.__speciality = speciality.upper()
            self.set_id()

    def get_salary(self):
        basic_salary = 3000
        print("The salary of the administrator", self.get_first_name(), self.get_last_name(), "is", end=" ")
        salary = str(round((basic_salary + (self.get_grade() / 100) * basic_salary), 2)) + "$"
        return salary

    def define(self):
        if self.get_middle_name():
            print("This is administrator", self.get_first_name(), self.get_last_name(),
                  self.get_middle_name(), "and his ID is: ", self.get_id())
        else:
            print("This is professor", self.get_first_name(), self.get_last_name(), "and his ID is: ", self.get_id())


def student_menu(logged_member: Student):
    print("Please select an operation:"
          "\n\t1)Change password"
          "\n\t2)Check marks"
          "\n\t3)Check your average")
    operation = int(input())
    while operation not in range(1, 4):
        operation = int(input("Wrong input, select operation again"))
    if operation == 1:
        logged_member.set_password()
    elif operation == 2:
        print("Informatics: ", logged_member.get_informatics(), "\n",
              "Mathematics: ", logged_member.get_maths(), "\n",
              "Electronics: ", logged_member.get_electronics())
    elif operation == 3:
        print("Yor average is: ", logged_member.get_average())
    return student_menu(logged_member)


def professor_menu(logged_member: Professor):
    print("Please select an operation:"
          "\n\t1)Change password"
          "\n\t2)Check students list"
          "\n\t3)Set students marks"
          "\n\t4)Get students marks")
    operation = int(input())
    while operation not in range(1, 5):
        operation = int(input("Wrong input, select operation again"))
    if operation == 1:
        logged_member.set_password()

    elif operation == 2:
        get_members_list(members[0])

    elif operation == 3:
        student_number = get_member_number(members[0])
        mark = int(input("Please enter a mark"))
        while mark not in range(0, 21):
            mark = int(input("Mark out of range! Please enter a correct mark: "))
        {
            "MATHS": members[0][student_number].set_math,
            "INFORMATICS": members[0][student_number].set_informatics,
            "ELECTRONICS": members[0][student_number].set_electronics
        }[logged_member.get_speciality()](mark)

    else:
        i = 1
        if logged_member.get_speciality() == "MATHS":
            for student in members[0]:
                print(str(i) + ")" + student.get_first_name() + " " + student.get_last_name() +
                      student.get_middle_name(), "\t\t", student.get_maths())

        elif logged_member.get_speciality() == "INFORMATICS":
            for student in members[0]:
                print(str(i) + ")" + student.get_first_name() + " " + student.get_last_name() +
                      student.get_middle_name(), "\t\t", student.get_informatics())
        else:
            for student in members[0]:
                print(str(i) + ")" + student.get_first_name() + " " + student.get_last_name() +
                      student.get_middle_name(), "\t\t", student.get_electronics())
        i += 1
    return professor_menu(logged_member)


def get_members_list(members_list):
    i = 1
    for member in members_list:
        print(str(i) + ")", member.get_first_name(), member.get_last_name(), member.get_middle_name())
        i += 1


def get_member_number(members_list):
    print("Please enter the number of the %s: " %
          ("student" if members_list == members[0] else
           "professor" if members_list == members[1] else
           "Administrator"), end="")
    member_number = int(input("> ")) - 1
    while member_number not in range(0, len(members_list)):
        member_number = int(input("Number out of range. Please enter the number again \n >  ")) - 1
    return member_number


def set_person_data(keyword, person: Person, data):
    if keyword == "first_name":
        person.set_first_name(data)
    elif keyword == "last_name":
        person.set_last_name(data)
    elif keyword == "middle_name":
        person.set_middle_name(data)
    elif keyword == "age":
        person.set_age(int(data))
    elif keyword == "email":
        person.set_email(data)
    elif keyword == "password":
        person.administrator_set_password(data)


def get_members_details(members_list):
    for i, member in enumerate(members_list, 1):
        print(str(i) + ")", end="")
        member.define()


def add_member(members_list):
    print("Please enter the data of the %s: " %
          ("student" if members_list == members[0] else
           "professor" if members_list == members[1] else
           "administrator"))
    if members_list == members[0]:
        member = Student("a", "a", 7, "a", "a", "a", 1)
        member.set_group_number(int(input("Enter group number")))
        Student.number_of_students += 1
    elif members_list == members[1]:
        member = Professor("a", "a", 7, "a", "a", "a", 11)
        member.set_teaching_hours(int(input("Enter teaching hours: ")))
        Professor.number_of_professors += 1
    else:
        member = Administrator("a", "a", 7, "a", "a", "a")
        Administrator.number_of_administrators += 1
    member.set_first_name(input("First name: "))
    member.set_last_name(input("Last name: "))
    member.set_age(input("Age "))
    member.administrator_set_password(input("Enter password "))
    member.set_grade(input("Enter grade ") if members_list == members[0]
                     else int(input("Enter grade ")))
    member.set_speciality(input("Enter speciality "))
    members_list.append(member)


def student_administrator_menu(logged_member: Administrator):
    print("Please select an operation:"
          "\n\t1)Change password"
          "\n\t2)Check students list"
          "\n\t3)Change student first name"
          "\n\t4)Change student last name"
          "\n\t5)Change student middle name"
          "\n\t6)Change student age"
          "\n\t7)Change student email"
          "\n\t8)Change student password"
          "\n\t9)Change student grade"
          "\n\t10)Change student speciality"
          "\n\t11)Change student group number"
          "\n\t12)Check student averages"
          "\n\t13)Check student details"
          "\n\t14)Add a new student"
          "\n\t%s" % "15)Back to the admin menu"
          if logged_member.get_speciality() == "ADMINS" else "")

    operation = int(input(">"))
    while operation not in range(1, 16):
        operation = int(input("Wrong input, select operation again"))
    if operation == 1:
        logged_member.set_password()
    elif operation == 2:
        get_members_list(members[0])
    elif operation in range(3, 9):
        student_number = get_member_number(members[0])
        data = input("Please enter data")
        set_person_data("first_name" if operation == 3
                        else "last_name" if operation == 4
        else "middle_name" if operation == 5
        else "age" if operation == 6
        else "email" if operation == 7
        else "password", members[0][student_number],
                        data)
    elif operation in range(9, 12):
        student_number = get_member_number(members[0])
        data = input("Please enter the data: ")
        {
            9: members[0][student_number].set_grade,
            10: members[0][student_number].set_speciality,
            11: members[0][student_number].set_group_number
        }[operation](int(data) if operation == 11 else data)
    elif operation == 12:
        student_number = get_member_number(members[0])
        print(members[0][student_number].get_average())
    elif operation == 13:
        get_members_details(members[0])
    elif operation ==14:
        add_member(members[0])
    else:
        if logged_member.get_speciality() == "ADMINS":
            return admins_menu(logged_member)
        else:
            print("Wrong operation")
    return student_administrator_menu(logged_member)


def professor_administrator_menu(logged_member: Administrator):
    print("Please select an operation:"
          "\n\t1)Change password"
          "\n\t2)Check professors list"
          "\n\t3)Change professor first name"
          "\n\t4)Change professor last name"
          "\n\t5)Change professor middle name"
          "\n\t6)Change professor age"
          "\n\t7)Change professor email"
          "\n\t8)Change professor password"
          "\n\t9)Change professor grade"
          "\n\t10)Change professor speciality"
          "\n\t11)Change professor teaching hours"
          "\n\t12)Check professor salary"
          "\n\t13)Check professor details"
          "\n\t14)Add a new professor"
          "\n\t%s" % ("15)Back to the admin menu"
          if logged_member.get_speciality() == "ADMINS" else ""))
    operation = int(input(">"))
    while operation not in range(1, 16):
        operation = int(input("Wrong input, select operation again"))
    if operation == 1:
        logged_member.set_password()
    elif operation == 2:
        get_members_list(members[1])
    elif operation in range(3, 9):
        professor_number = get_member_number(members[1])
        data = input("Please enter data")
        set_person_data("first_name" if operation == 3
                        else "last_name" if operation == 4
        else "middle_name" if operation == 5
        else "age" if operation == 6
        else "email" if operation == 7
        else "password", members[1][professor_number],
                        data)
    elif operation in range(9, 12):
        professor_number = get_member_number(members[1])
        data = input("Please enter the data: ")
        {
            9: members[1][professor_number].set_grade,
            10: members[1][professor_number].set_speciality,
            11: members[1][professor_number].set_group_number
        }[operation](data if operation == 10 else int(data))
    elif operation == 12:
        professor_number = get_member_number(members[1])
        print(members[1][professor_number].get_salary())
    elif operation == 13:
        get_members_details(members[1])
    elif operation == 14:
        add_member(members[1])
    else:
        if logged_member.get_speciality() == "ADMINS":
            return admins_menu(logged_member)
        else:
            print("Wrong operation")
    return professor_administrator_menu(logged_member)

def admins_menu(logged_member: Administrator):
    print("Please select what you want to manage: "
          "\n\t1)Manage Administrators"
          "\n\t2)Manage Professors"
          "\n\t3)Manage Students")
    manage = int(input("> "))
    while manage not in (1, 2, 3):
        manage = int(input("Wrong choice, please enter a valid option"))
    def administrator_administrator_menu(logged_member: Administrator):
        print("Please select an operation:"
              "\n\t1)Change password"
              "\n\t2)Check administrators list"
              "\n\t3)Change administrator first name"
              "\n\t4)Change administrator last name"
              "\n\t5)Change administrator middle name"
              "\n\t6)Change administrator age"
              "\n\t7)Change administrator email"
              "\n\t8)Change administrator password"
              "\n\t9)Change administrator grade"
              "\n\t10)Change administrator speciality"
              "\n\t11)Change administrator salary"
              "\n\t12)Check administrator details"
              "\n\t13)Add a new administrator"
              "\n\t14)Back to the admin menu"
              if logged_member.get_speciality() == "ADMINS" else "")
        operation = int(input(">"))
        while operation not in range(1, 15):
            operation = int(input("Wrong input, select operation again"))
        if operation == 1:
            logged_member.set_password()
        elif operation == 2:
            get_members_list(members[2])
        elif operation in range(3, 9):
            administrator_number = get_member_number(members[2])
            data = input("Please enter data")
            set_person_data("first_name" if operation == 3
                            else "last_name" if operation == 4
            else "middle_name" if operation == 5
            else "age" if operation == 6
            else "email" if operation == 7
            else "password", members[2][administrator_number],
                            data)
        elif operation in range(9, 12):
            administrator_number = get_member_number(members[2])
            data = input("Please enter the data: ")
            {
                9: members[2][administrator_number].set_grade,
                10: members[2][administrator_number].set_speciality,
            }[operation](data if operation == 10 else int(data))
        elif operation == 11:
            administrator_number = get_member_number(members[2])
            print(members[2][administrator_number].get_salary())
        elif operation == 12:
            get_members_details(members[2])
        elif operation == 13:
            add_member(members[2])
        else:
            return admins_menu(logged_member)
        return administrator_administrator_menu(logged_member)


    {
        1: administrator_administrator_menu,
        2: professor_administrator_menu,
        3: student_administrator_menu
    }[manage](logged_member)


members = [[Student("Isai", "Fomperoza", 22, "1234567", "first", "python", 10)],
           [Professor("jimmy", "jahn", 30, "qwerty", 5, "Maths", 25)],
           [Administrator("farid", "cena", 35, "asdfg", 5, "professors")]]

print("\t\t\t\t\t\t\t**Welcome to our school system**\n\n "
      "Please enter your profession\n\n"
      "1) Student\n"
      "2) Professor\n"
      "3)Administrator")
profession = int(input("> ")) - 1
while profession not in range(0, 3):
    profession = int(input("Wrong choice, please enter a profession")) - 1
logged_member = None
while not logged_member:
    email = input("Please enter your email")
    for member in members[profession]:
        if member.get_email() == email:
            password = input("Enter your password:  ")
            for i in range(4):
                if password == member.get_password():
                    print("Hallo ", member.get_first_name(), member.get_last_name(), "!")
                    logged_member = member
                    break
                else:
                    password = input("Wrong password! Enter your password:  ")
            break
    if not logged_member:
        print("Incorrect information")
if profession == 0:
    student_menu(logged_member)

elif profession == 1:
    professor_menu(logged_member)
else:
    if logged_member.get_speciality() == "STUDENTS":
        student_administrator_menu(logged_member)
    elif logged_member.get_speciality() == "PROFESSORS":
        professor_administrator_menu(logged_member)
    elif logged_member.get_speciality() == "ADMINS":
        admins_menu(logged_member)
    else:
        print("Wrong input")
