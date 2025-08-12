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


        def add_course(self,course):
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

