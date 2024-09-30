#TO ADD TWO NUMBERS
def add(n1 , n2):
    print(num1,'+',num2,'=',num1+num2)


#TO SUBTRACT TWO NUMBERS
def subtract(n1 , n2):
    print(num1,'-',num2,'=',num1-num2)


#TO MULTIPLY TWO NUMBERS
def multiply(n1 , n2):
    print(num1,"*",num2,"=",num1*num2)


#TO DIVIDE TWO NUMBERS
def divide(n1 , n2):
    if num1>=num2:
        print(num1,'/',num2,'=',num1/num2)
    else:
        print("Invalid!!!")


#TO FIND THE POWER OF A NUMBER
def power(n1 , n2):
    if n1==0:
        print("Invalid!!!")
    else:
        print(num1,"**",num2,'=',num1**num2)


# To check if the user wants to keep calculating
Keep_Calc=True

print("WELCOME TO THIS SIMPLE CALCULATOR for solving your basic problems\n \n")
print("So, What are you waiting for..?\n\n")
print("LETS GET STARTED!!!\n")

while Keep_Calc is True:

    #INPUTTING THE FIRST NUMBER FROM USER
    num1=float(input("Enter the first number: "))

    #INPUTTING THE SECOND NUMBER FROM USER
    num2=float(input("Enter the second number: "))

    #THE BASIC ARITHMETIC OPERATIONS
    print("1) add \n")
    print("2) subtract\n")
    print("3) multiply\n")
    print("4) divide\n")
    print("5) power\n")


    #ASKING  USER'S  CHOICE OF ARITHMETIC OPERATION
    basic_op=input("Enter name of the arithmetic operation from above correctly : \n")

    #Checking if the operation chosen is to  add
    if basic_op=="add":
        add(num1 , num2)


    #Checking if the operation chosen is to subtract
    elif basic_op=="subtract":
        subtract(num1 , num2)


    #Checking if the operation chosen is to multiply
    elif basic_op == "multiply":
        multiply(num1 , num2)


    #Checking if the operation chosen is to divide
    elif basic_op == "divide":
        divide(num1 , num2)


    #Checking if the operation chosen is to find the power
    elif basic_op =="power":
        power(num1 , num2)

    #Checking if the operation chosen is  incorrect
    else:
        print("Invalid!  Try Again!!!")

    print("\nDONE!!!\n")

    Lets_Calc=input("Do you want to keep calculating? [ yes / no ]\n")

    if Lets_Calc== "yes":
        print("\nGreat!\nLets Go For the Next One !!\n\n")
        continue

    elif Lets_Calc== "no":
        print("\n\n#############\nNo Problem!\nBye!\nHave a great day ahead!!!\n############\n\n")
        Keep_Calc=False

    else:
        break

