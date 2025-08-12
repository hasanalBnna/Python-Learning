import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {self.name} in {subject}.")
        else:
            print(f"{self.name} is not enrolled in {subject}.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_student_info(self):
        print(f"Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self.course_name)
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        print(f"Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for student in self.students])}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age, address, student_id)
            print(f"Student {name} (ID: {student_id}) added successfully.")
        else:
            print(f"Student ID {student_id} already exists.")

    def add_course(self, course_name, course_code, instructor):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_name, course_code, instructor)
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")
        else:
            print(f"Course code {course_code} already exists.")

    def enroll_student_in_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            self.courses[course_code].add_student(self.students[student_id])
            print(f"Student {self.students[student_id].name} (ID: {student_id}) enrolled in {self.courses[course_code].course_name} (Code: {course_code}).")
        else:
            print("Invalid student ID or course code.")

    def add_grade(self, student_id, course_code, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(course_code, grade)
        else:
            print("Invalid student ID.")

    def display_student_details(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Invalid student ID.")

    def display_course_details(self, course_code):
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Invalid course code.")

    def save_data(self, filename):
        data = {
            "students": {student_id: vars(student) for student_id, student in self.students.items()},
            "courses": {course_code: vars(course) for course_code, course in self.courses.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for student_id, student_info in data['students'].items():
                    student = Student(student_info['name'], student_info['age'], student_info['address'], student_id)
                    student.grades = student_info['grades']
                    student.courses = student_info['courses']
                    self.students[student_id] = student
                
                for course_code, course_info in data['courses'].items():
                    course = Course(course_info['course_name'], course_code, course_info['instructor'])
                    self.courses[course_code] = course
                    for student_id in course_info['students']:
                        if student_id in self.students:
                            course.add_student(self.students[student_id])
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        
        option = input("Select Option: ")
        
        if option == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            sms.add_student(name, age, address, student_id)
        
        elif option == '2':
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            sms.add_course(course_name, course_code, instructor)
        
        elif option == '3':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            sms.enroll_student_in_course(student_id, course_code)
        
        elif option == '4':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            sms.add_grade(student_id, course_code, grade)
        
        elif option == '5':
            student_id = input("Enter Student ID: ")
            sms.display_student_details(student_id)
        
        elif option == '6':
            course_code = input("Enter Course Code: ")
            sms.display_course_details(course_code)
        
        elif option == '7':
            filename = input("Enter filename to save data: ")
            sms.save_data(filename)
        
        elif option == '8':
            filename = input("Enter filename to load data: ")
            sms.load_data(filename)
        
        elif option == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
