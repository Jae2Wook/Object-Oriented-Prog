from collections import deque

class Student:

    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        print("{} for {}".format(self.name, self.course))

class HelpSystem:

    def __init__(self):
        self.waiting_list = deque() # 2. linked to Student() by .append

    def is_student_waiting(self):
        return len(self.waiting_list) > 0

    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)  # 1. Student() enters

    def help_next_student(self):
        if self.is_student_waiting():
            student = self.waiting_list.popleft() # 3. So I can use Student() through linked waiting_list
            print("Helping:")
            student.display()
            if self.is_student_waiting():
                print("Get ready: ")
                student = self.waiting_list[0]
                student.display()

        else:
            print("No one to help.")


def main():

    opt = 0
    help = HelpSystem() # For deque() is outside the loop to record?
    while opt != 3:
        print("Oprions: ")
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        opt = int(input("Enter selection: "))
        print()
        if opt == 1:
            student = Student()
            student.prompt()
            help.add_to_waiting_list(student) # How Student() goes into HelpSystem()
        if opt == 2:
            help.help_next_student()
        

    print("Goodbye")
            


if __name__ == "__main__":
    main()