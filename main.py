# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Student import Student


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def take_input():
    ch = int(input("Enter choice:"))
    return ch
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
# an object of Student class
    obj = Student('', 0, 0, 0)
    print(
    "\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
    while(True):
        c = take_input()
        if(c == 1):
            name = input("Enter Student's name:")
            roll = int(input("Enter Student's Roll no:"))
            marks1 = int(input("Enter Student's Marks 1:"))
            marks2 = int(input("Enter Student's Marks 2:"))
            obj.accept(name, roll, marks1, marks2)
            obj.accept("B", 2, 64, 55)
            obj.accept("C", 3, 12, 33)
            obj.accept("D", 4, 78, 77)
            obj.accept("E", 5, 56, 98)
            obj.accept("F", 6, 65, 89)
            obj.accept("J", 8, 78, 87)
            obj.accept("H", 7, 96, 32)
            obj.accept("I", 9, 74, 44)

    # This is a comment line to see if Git is connected to this. This is added the next time
        elif(c == 2):
            print("\n")
            print("\nList of Students\n")
            for i in range(len(obj.ls)):
                obj.display(obj.ls[i])

        elif(c == 3):
            print("\n Student Found, ")
            s = obj.search(2)
            obj.display(obj.ls[s])

        elif(c == 4):
            obj.delete(2)
            print(len(obj.ls))
            print("List after deletion")
            for i in range(len(obj.ls)):
                obj.display(obj.ls[i])

        elif(c == 5):
            obj.update(3, 2)
            print(len(obj.ls))
            print("List after updation")
            for i in range(len(obj.ls)):
                obj.display(obj.ls[i])
        else:
            print("Thank You !")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
