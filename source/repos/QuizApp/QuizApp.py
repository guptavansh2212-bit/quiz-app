print("-------------- Student's Personal Details -----------------")
Student_name=input("Enter your name: ")
course_name=input("Enter your Course: ")
University_Name=input("Enter your University name: ")
Student_Emailid=input("Enter your Email ID: ")
print("Which programming language are you interested in? : ")
print("1. C")
print("2. Java")
print("3. Python")
print("4. HTML")

while True:
    choice=input("Student's choice(1-4): ")
    if choice=="1":
        language="C"
        break
    elif choice=="2":
        language="Java"
        break
    elif choice=="3":
        language="Python"
        break
    elif choice=="4":
        language="HTML"
        break
    else:
        print("Invalid Choice")
print(f"You selected {language}.")

while True:
     participate=input("Do you want to participate in quiz(yes/no) : ")
     if participate=="yes":
         print(f"Welcome {Student_name}! Get ready for {language} quiz")
         print("Believe in yourself. All the best!!\n")
         break
     elif participate=="no":
         print("Okay, Thank you. Goodbye!")
         exit()
     else:
         print("Invalid Input. Please Try Again")
print("_____________________________________________________________")
         ## -------------- C Programming language ----------------------- ##
score=0
if language=="C":
    print(f"\n Q1.Which of the following keyword has 8 bytes?")
    print(f"\n a.int")
    print(f"\n b.char")
    print(f"\n c.float")
    print(f"\n d.double")
    answer=input("Your answer(a-d): ")
    if answer=="d":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q2.What is the output of a given code?")
    print(f'\n printf("%d", 5/2);')
    print(f"\n a.2.5")
    print(f"\n b.2")
    print(f"\n c.3")
    print(f"\n d.2.0")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q3.What causes a memory leak in C?")
    print(f"\n a.Using too many variables")
    print(f"\n b.Allocating memory dynamically and never freeing it")
    print(f"\n c.Using a pointer to an array")
    print(f"\n d.Declaring a global value")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q4.Which method is used to pass the memory address of a variable to a function?")
    print(f"\n a.Call by Reference")
    print(f"\n b.Call by Value")
    print(f"\n c.Call by Name")
    print(f"\n d.Call by Copy")
    answer=input("Your answer(a-d): ")
    if answer=="a":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
        ## -------------- Java Programming language ----------------------- ##
elif language=="Java":
    print(f"\n Q1.Which of the following features is not correct about Java? ")
    print(f"\n a.Java is based on Object Oriented Programming ")
    print(f"\n b.They have clean syntax which is inspired from C and C++")
    print(f"\n c.Java have does not any platform independent")
    print(f"\n d.Java is designed to handle such runtime errors and handles the exception")
    answer=input("Your answer(a-d): ")
    if answer=="c":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q2.What is the output of this Java Code? ")
    print(f"\n int x = 10;")
    print(f"\n System.out.println(x++ + ++x);")
    print(f"\n a.20")
    print(f"\n b.21")
    print(f"\n c.22")
    print(f"\n d.23")
    answer=input("Your answer(a-d): ")
    if answer=="c":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q3.Why Java have does not have pointer like C++? ")
    print(f"\n a.Due to Security risks, maintaining memory management and ensuring simplicity")
    print(f"\n b.Due to NullPointerException")
    print(f"\n c.Reference values are the pointers")
    print(f"\n d.None of the Above")
    answer=input("Your answer(a-d): ")
    if answer=="a":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q4.Which Exception is raised for an arithmetic error? ")
    print(f"\n a.ArrayIndexOutofBoundsException")
    print(f"\n b.NullPointerException")
    print(f"\n c.ArithmeticException")
    print(f"\n d.NumberFormatException")
    answer=input("Your answer(a-d): ")
    if answer=="c":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
        ## -------------- Python Programming language ----------------------- ##
elif language=="Python":
    print(f"\n Q1.Which of the following have key:value pair?")
    print(f"\n a.List")
    print(f"\n b.Dictionary")
    print(f"\n c.Tuple")
    print(f"\n d.Set Object")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q2.What would be the correct output of this code?")
    print(f'\n S = "Python"')
    print(f"\n print(S*3)")
    print(f"\n a.Python Python Python")
    print(f"\n b.PythonPythonPython")
    print(f"\n c.python")
    print(f"\n d.pythonpythonpython")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q3.What would be the correct output of this code?")
    print(f"\n print(round(123.456,-2))")
    print(f"\n a.100.0")
    print(f"\n b.120.0")
    print(f"\n c.123.0")
    print(f"\n d.130.0")
    answer=input("Your answer(a-d): ")
    if answer=="a":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q4.Which of the following is not a feature of Python?")
    print(f"\n a.Simple and Easy to learn")
    print(f"\n b.Interpreter")
    print(f"\n c.Object Oriented Programming")
    print(f"\n d.Requires manual memory management")
    answer=input("Your answer(a-d): ")
    if answer=="d":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
        ## -------------- HTML ----------------------- ##
elif language=="HTML":
    print(f"\n Q1.Which Tag is used for Hyperlink Reference?")
    print(f"\n a.<br>")
    print(f"\n b.<a>")
    print(f"\n c.<button>")
    print(f"\n d.<style>")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q2. Which Tag is used to make Next Line?")
    print(f"\n a.<br>")
    print(f"\n b.<p>")
    print(f"\n c.<hr>")
    print(f"\n d.<pre>")
    answer=input("Your answer(a-d): ")
    if answer=="a":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q3. Which option is correct about <strong> and <b> tags?")
    print(f"\n a.Both are semantic elements")
    print(f"\n b.<strong> marks importance and <b> is only used to make the text bold")
    print(f"\n c.Both are deprecated")
    print(f"\n d.Both tags are completely interchangeable")
    answer=input("Your answer(a-d): ")
    if answer=="b":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
    print(f"\n Q4. Which tag is used to insert an image?")
    print(f"\n a.<li>")
    print(f"\n b.<a>")
    print(f"\n c.<img src="">")
    print(f"\n d.<pre>")
    answer=input("Your answer(a-d): ")
    if answer=="c":
        print("Correct Answer")
        score+=2
    else:
        print("Wrong Answer")
total=8
percentage = score/total*100
print("-- RESULT -- ")
print(f"Name:{Student_name}")
print(f"Language:{language}")
print(f"Score:{score}/{total}")
print(f"Percentage:{percentage:.2f}%")

if(percentage>=80):
    print("Excellent Performance!!")
elif(percentage>=60):
    print("Good!!")
elif(percentage>=40):
    print("Needs to improvement")
else:
    print("Keep practicing, you could do better!")
print("End of Program!!")