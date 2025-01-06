class Student:
    def __init__(self, name, marks):
        """
        Constructor to initialize student name and marks for 5 subjects.
        :param name: str: Name of the student
        :param marks: list: List of marks in 5 subjects
        """
        self.name = name
        self.marks = marks

    def calculate_average(self):
        """
        Function to calculate the average marks of the student.
        :return: float: Average of the marks
        """
        total_marks = sum(self.marks)
        average = total_marks / len(self.marks)
        return average

    def display_average(self):
        """
        Function to print the average marks of the student.
        """
        avg = self.calculate_average()
        print(f"Student: {self.name}, Average Marks: {avg:.2f}")



marks = [85, 90, 78, 88, 92]  # Marks in 5 subjects
student = Student("John", marks)
student.display_average()
