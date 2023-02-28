class Student:

    # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # Create a list to add Students
    ls = []

    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
        # use ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2)
        self.ls.append(ob)
        self.display(ob)

    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")

    # Search Function
    def search(self, rn):
        for i in range(self.ls.__len__()):
            if (self.ls[i].rollno == rn):
                return i

    # Delete Function
    def delete(self, rn):
        i = self.search(rn)
        del self.ls[i]

    # Update Function
    def update(self, rn, No):
        i = self.search(rn)
        roll = No
        self.ls[i].rollno = roll