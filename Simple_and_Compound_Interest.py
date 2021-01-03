import time
Y="y"
while Y in "yY":
    print('''First of all Thank you for choosing this option
            Then, next i will help you find the Simple interest and Compound interest
            in this module, but for that kindly fill the questions below with a 
            \'Y\' for yes and \'N\' for No''')
    time.sleep(1.5)
    SI=input("Do you want to find SI (Simple Interest):")
    print("Now don\'t be a thug, Enter the right values in numbers")
    P=float(input("Enter the principle amount:"))
    R=float(input("Enter rate of Interest(in%):"))
    T=float(input("Enter the time period (in Years): "))
    interest_SI = (P * R * T) / 100
    interest_CI = P * ((1 + (R / 100))**T)
    time.sleep(1.5)
    if SI=="Y" or SI=="y":
        print("The Simple interest amount is",interest_SI)
        time.sleep(2)
        print("*" * 15)
        print("If you had taken this loan with CI then the interest would have been ",interest_CI)
        print("Which is",interest_CI/interest_SI,"times")
        print("*" * 15)
        time.sleep(1)
    elif SI=='n' or SI=="N":
        print("The Compound interest amount is", interest_CI)
        time.sleep(2)
        print("*"*15)
        print("If you had taken this loan with SI then the interest would have been ", interest_SI)
        print("!!Which is", interest_SI / interest_CI, "times!!")
        print("*" * 15)
        time.sleep(1)
    Y = input("Do you still want to continue(Y/N):")
    time.sleep(1)
    print("-" * 80)