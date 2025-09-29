print("hello world ")
print("hello everyone this is my first project ")
while True:
    print("Welcome To Calculator")
    while True:
        try:
            a= int(input("Please Enter First Number = "))
        except ValueError:
            print("❌ Please Enter Number Between 0-999999999... ")
        else:
            break
    while True:
        try:
            b= int(input("Please Enter Second Number = "))
        except ValueError:
            print("❌ Please Enter Number Between 0-999999999... ")
        else:
            break
    print("Please Select arithmetic operator from the given options below")
    print("For Adduition please Enter ( + ) ")
    print("For Subtract please Enter ( - ) ")
    print("For Multiplication please Enter ( * ) ")
    print("For Division please Enter ( / ) ")
    while True:
        Operator = input("Please Enter Oprater (+, -, *, / ) ")
        if Operator == '+':
            print("You selected Addition ")
            print("Your Answer is = ", (a+b))
            break
        elif Operator == '-':
            print("You selected Subtract")
            print("Your Answer is = ", (a-b))
            break
        elif Operator == '*':
            print("You selected Multiplication")
            print("Your Answer is = ", (a*b))  
            break    
        elif Operator == '/':
            print("You selected Division")
            print("Your Answer is = ", (a/b))
            break
        else:
            print("❌ Invalid operator. Please enter one of +, -, *, /.") 
    x = str.upper(input("Press any key to Continue or 'E' for Exit "))
    if x == 'E':
    print("thanks")
    break
