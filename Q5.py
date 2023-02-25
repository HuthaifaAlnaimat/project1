#Q5) write a program to show a menu for school the menu should be
#1- add class
#2- add student to class
#3- print the whole school
#4- print specific student
#5- exit

clases=[None]
std=[None]
dictenery={

}
while True:
    print("please input your choice")
    print("1- add class")
    print("2- add student to class")
    print("3- print the whole school")
    print("4- print specific student")
    print("5- exit")
    if num == "1":
        classes = input("Please enter class name or number\n")
        clases.append(classes)
    elif num == "2":
        s = input("Please enter the name of the student\n")
        n = int(input("Please enter the index of the class that u want to student in it \n"))
        dictenery[s] = clases[n]
    elif num == "3":
        print("There is the all students in the school with the classes", dictenery)
    elif num == "4":
        print("Please enter the name of the student to know what is his class")
        Name = input()
        print(dictenery[Name])
    elif num == "5":
        print("Thanks for using our program")
        break
    else:
        print("Sorry u entered wrong value can u please reenter one of the 5 choices")