import time
Y='y'
print('''First of all Thank you for choosing this option
            Then, next i will help you find your BMI here
            If you ask me what are the prerequisites for this ,
            1) Your height(in metre)
            2) Your Weight(in KG)''')
time.sleep(1.5)
while Y in "yY":
    W=float(input("Enter your weight(KG):"))
    H=float(input("Enter your height(metre):"))
    age=float(input("Enter your age:"))
    S=input("By what sex would you like to be known (Male or Female):")
    BMI=W/H**2
    if S.lower() == "male" :
        if age <= 10:
            if BMI<=17.5:
                print("Your BMI is",BMI,"which means you are under-weight")
                print("The average BMI is 24.1")
            elif BMI>17.5 and BMI <= 25:
                print("Your BMI is",BMI,"which means you have a very normal BMI!")
                print("The average BMI is 24.1")
            elif BMI>25 and BMI <= 30:
                print("Your BMI is", BMI, "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 24.1")
            elif BMI>30 and BMI <= 35:
                print("Your BMI is",BMI,"which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 24.4")
            elif BMI>35 and BMI<=40:
                print("Your BMI is",BMI,"which means currently you are in Obese class II")
                print("The average BMI is 19.3")

        elif age > 20 and BMI<=29:
            if BMI <= 18.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 24.3")
            elif BMI > 18.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 24.3")
            elif BMI > 25 and BMI <= 30:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 24.3")
            elif BMI > 30 and BMI <= 35.4:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 24.3")
            elif BMI > 35.4 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 24.3")

        elif age > 29 and BMI<=39:
            if BMI <= 18.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 21")
            elif BMI > 18.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 21")
            elif BMI > 25 and BMI <= 29:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 21")
            elif BMI > 29 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 21")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 21")

        elif age > 39 and BMI<=69:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 21")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 21")
            elif BMI > 25 and BMI <= 30.4:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 21")
            elif BMI > 30.4 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 21")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 21")

        elif age > 69 and BMI<=99:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 23.4")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 23.4")
            elif BMI > 25 and BMI <= 32:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 23.4")
            elif BMI > 32 and BMI <= 37:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 23.4")
            elif BMI > 37 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 23.4")

        else:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 25")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 25")
            elif BMI > 25 and BMI <= 30:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 25")
            elif BMI > 30 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 25")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 25")

    if S.lower() == "female" :
        if age <= 10:
            if BMI <= 16.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 18.6")
            elif BMI > 16.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 18.6")
            elif BMI > 25 and BMI <= 29:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 18.6")
            elif BMI > 29 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 18.6")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 18.6")

        elif age > 20 and BMI <= 29:
            if BMI <= 18.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 24.1")
            elif BMI > 18.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 24.1")
            elif BMI > 25 and BMI <= 30:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 24.1")
            elif BMI > 30 and BMI <= 35.4:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 24.1")
            elif BMI > 35.4 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 24.1")

        elif age > 29 and BMI <= 39:
            if BMI <= 18.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 18.9")
            elif BMI > 18.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 18.9")
            elif BMI > 25 and BMI <= 29:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 18.9")
            elif BMI > 29 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 18.9")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 18.9")

        elif age > 39 and BMI <= 69:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 24")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 24")
            elif BMI > 25 and BMI <= 30.4:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 24")
            elif BMI > 30.4 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 24")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 24")

        elif age > 69 and BMI <= 99:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 23.6")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 23.6")
            elif BMI > 25 and BMI <= 32:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 23.6")
            elif BMI > 32 and BMI <= 37:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 23.6")
            elif BMI > 37 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 23.6")

        else:
            if BMI <= 17.5:
                print("Your BMI is", BMI, "which means you are under-weight")
                print("The average BMI is 24.6")
            elif BMI > 17.5 and BMI <= 25:
                print("Your BMI is", BMI, "which means you have a very normal BMI!")
                print("The average BMI is 24.6")
            elif BMI > 25 and BMI <= 30:
                print("Your BMI is", BMI,
                      "which means according to your BMI there is an extra-thing in you(You can do well, but currently you are over-weight")
                print("The average BMI is 24.6")
            elif BMI > 30 and BMI <= 35:
                print("Your BMI is", BMI, "which means there is an extra-extra butter with you, Currently in Obese class I")
                print("The average BMI is 24.6")
            elif BMI > 35 and BMI <= 40:
                print("Your BMI is", BMI, "which means currently you are in Obese class II")
                print("The average BMI is 24.6")
    Y = input("Do you still want to continue(Y/N):")