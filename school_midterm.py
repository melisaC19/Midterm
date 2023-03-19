import csv


class School:
    def __init__(self):

        # student data structure
        self.students = {}
        self.courses = {}
        self.enrollments = {}

        self.read_students()
        self.read_courses()
        self.read_enrollments()

    def read_students(self):

        # read the student.csv
        f = open('students.csv')

        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row[1] != ' name':
                # print(row)
                self.students[row[0]] = {'id': int(row[0]), 'name': row[1], 'email': row[2]}

    def read_courses(self):

        # read the courses.csv
        f = open('courses.csv')

        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row[1] != ' name':
                # print(row)
                self.courses[row[1]] = {'id': row[0], 'name': row[1], 'credit': row[2]}

    def read_enrollments(self):

        # read the enrollments.csv
        f = open('enrollments.csv')

        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if row[1] != ' course id':
                # print(row)
                # student id, course id, semester, grade
                # key = student_id + '-' + course_id
                self.enrollments[row[0] + '-' + row[1]] = {'student_id': int(row[0]), 'course_id': row[1],
                                                           'semester': row[2], 'grade': row[3]}

    def add_student(self):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        email = input("Enter student email: ")

        self.students[id] = {'id': int(id), 'name': name, 'email': email}
        print("Student added successfully")

    def enroll_student(self):
        student_id = input("Enter student id: ")
        course_id = input("Enter course id: ")
        semester = input("Enter semester: ")

        key = student_id + '-' + course_id

        if key in self.enrollments:
            print("The student is already enrolled in the course")
        else:
            self.enrollments[key] = {'student_id': int(student_id), 'course_id': course_id, 'semester': semester}
            print("Student enrolled successfully")

    def grade_student(self):
        student_id = input("Enter student id: ")
        course_id = input("Enter course id: ")
        key = student_id + '-' + course_id

        if key in self.enrollments:
            grade = input("Enter grade: ")
            self.enrollments[key]['grade'] = grade
            print("Grade updated successfully")
        else:
            print("The student is not enrolled in the course")

    def display_student(self):
        print('What Student you wish to display?')
        student_id = input('Student id: ')

        # look for student in dictionary
        if student_id in self.students:
            student_info = self.students[student_id]
            print(student_info)

            # get all course of student
            enrolled_courses = []
            for k, v in self.enrollments.items():
                if v['student_id'] == int(student_id):
                    enrolled_courses.append(v)

            if enrolled_courses:
                print("Enrolled courses:")
                for course in enrolled_courses: 
                    print(course)


#calling school 
school_obj = School()


exit = False

while exit == False:
    print("1. Add Student")
    print("2. Enroll Student to Course")
    print("3. Grade Student")
    print("4. Display Student")
    print("5. Display Course")
    print("0. EXIT")

    option = input("Choose an option: ")

    #EXIT
    if option == '0':
        print('your operation has ended')
        exit = True

    #option 1 add student 
    if option == '1':
        school_obj.add_student()

    #optiun 2 enrolling a student to courses
    if option == '2':
        school_obj.enroll_student()

    #option 3 grade student 
    if option == '3':
        school_obj.grade_student()

    #option 4 display student
    if option == '4': 
        school_obj.display_student()
    #display course 
    if option == '5':
        print('What Course you wish to display?')
        course = input('Course name: ')
        #look for course in dictionary 
        try:
            results = school_obj.courses[course]
            print(results)
        except:
            print(course + " isn't available !")
            


    print("\n\n")


