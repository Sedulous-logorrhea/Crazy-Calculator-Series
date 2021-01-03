#-------------------------------------------The Calculator----------------------------------------------------
import time
from random import *
from turtle import *

from covid import Covid
from matplotlib import pyplot as plt
time.sleep(.5)
print('''Welcome to my Computer Science Winter holiday\'s Project work
        Here i am introducing you this application of mine which i have named it as 
        Calculator which i thought will be able to express itself with its name.''')

print('''So lets begin''',time.sleep(1),
      '''⩹𝑢𝑢𝑢First of all this is going to be in form of a menu-driven program,
         So you will need to select the appropriate number to choose the right option,
         If you think you have made mistake then continue untill the loop ends,
         then reselect the option and get the right answer. Whenever you want to leave,
         you can leave with esc button or by typing n/N when the command prompts you to.𝑢𝑢𝑢⩺''',
        time.sleep(2))
C="y"
while C in "yY":
    print('''The list of selections are:-
                1       <-      BMI Calculator
                2       <-      Covid Calculator
                3       <-      PMI Simple and Compound interest
                4       <-      Budget calculator
                5       <-      Simple Calculator''')
    sel=int(input("Enter the right option favourable to you:"))

# -------------------------------------------BMI Calculator----------------------------------------------------
    if sel==1:

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

# -------------------------------------------Covid Calculator----------------------------------------------------

    elif sel==2:
        Y="y"
        print( '''Hello everyone,this section does not contain a 100% accurate data
              But.... for an approximate data, i am pleased to know you have chose this option.
              As we all know that the pandemic has made the busy world to stand still
              But i will argue that this wasn\'t all negative, this is digitally a blessing in disguise
              So without any more further delay lets proceed.......''')
        random_stuffs=['''Pandemic : A pandemic is an epidemic of an infectious disease that 
                has spread across a large region, for instance multiple continents or worldwide,
                affecting a substantial number of people.''',"CoViD-19 : Corona Virus Disease 2019 or SARS-CoV-2","Anosmia (loss of smell) is a symptom.","SARS-CoV-2 binds tightly to human cells.",'''Compared to adults, children appear much less likely to get sick if they contract the novel coronavirus. 
                However, the very young (less than 1 year) appear to be more vulnerable to serious illness than older children.''','''Researchers have found that the virus can live up to 24 hours on cardboard and 2 to 3 days on plastic and stainless steel.\n
                The CDC reports that the virus was detected on surfaces of the Diamond Princess cruise ship up to 17 days after passengers disembarked. \n However, only pieces of the virus were detectable, not viruses capable of infecting a person.''',"The CDC estimates up to 40% of infected individuals do not experience symptoms. ",'''People with type A blood 
                may be more susceptible to infection.''','''Some people never develop symptoms.
                And some people who had what they thought was a “bad cold” or the flu may have actually had COVID-19.''']
        time.sleep(2)
        covid=Covid()
        list_of_countries=covid.list_countries()
        while Y in "yY":
            N=randint(0,8)
            print("Before we begin Lets have a fact check")
            time.sleep(1.5)
            print(random_stuffs[N])
            time.sleep(2.2)
            list_of_countries=covid.list_countries()
            Assistance=input("Do you need assistance on the list of countries(Y/N):")
            if Assistance=="y" or Assistance=="Y":
                print(list_of_countries)
            country=input("Enter which country you want the covid cases report for:")
            time.sleep(1)
            cases=covid.get_status_by_country_name(country)
            for x in cases:
                print(x,":",cases[x])
                time.sleep(1)
            Y=input("Do you still want to continue(Y/N):")
            time.sleep(1)
            print("-"*80)

# -------------------------------------------PMI SI and CI----------------------------------------------------

    elif sel==3:
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

# -------------------------------------------Budget Calculator----------------------------------------------------

    elif sel==4:
        time.sleep(1)
        print('''For starters , Let me introduce you to my humble little budget_Calculator.
                With this program you will be able to get an approximate image of your spending 
                in reference to your income. I hope to provide an overall comparison of your income-expense
                data with the average income-expense of a normal person of similar background ''')
        time.sleep(.5)
        term=input("Do you want a yearly or monthly report (Y/M) :")

        #Imp terms
        L_income=["Salary",]
        L_income_m=[]
        L_expenses=[]
        L_expenses_m=[]
        P_bal=[]

        #income
        if term in "Yy":
            print("So you choose to select yearly report ")
            salary=int(input("What is your monthly salary:"))
            L_income_m.append(salary * 12)
            overtime=input("Do you get paid for overtime(Y/N):")
            if overtime in "yY":
                overtime_m=int(input("How much are you paid for overtime per hour: "))
                freq=int(input("How many hours do you get overtime per year:"))
                L_income.append("Overtime")
                L_income_m.append(overtime_m * freq)
            else:
                overtime_m=0
            Bonus = input("Do you get bonus yearly (Y/N):")
            if Bonus in "yY":
                Bonus_m = int(input("How much are you paid yearly in Bonus: "))
                L_income.append("Bonus")
                L_income_m.append(Bonus_m)
            else:
                Bonus_m=0
            Other_benefits=input("Do you have any other medium of getting paid (Y/N) ? :")
            if Other_benefits in "Yy":
                n_benefits=int(input("How many other ways?:"))
                for i in range(n_benefits):
                    L_income.append(input("Enter the way:"))
                    L_income_m.append(int(input("Enter the amount:")))
            print("So your total number of ways of earning is",len(L_income))
            print("i.e")
            for i in range(len(L_income)):
                print(L_income[i],end=",")
            T_income_m=(sum(L_income_m)-salary)+salary*12
            print("So your total yearly income is",T_income_m)
            Tot_income_m=T_income_m
            M_balance=T_income_m

        #Expense
            H_rent = input("Do you have a rented home(Y/N):")
            if H_rent in "yY":
                H_rent_m = int(input("How much do you pay for home rent: "))
                L_expenses.append("Home rent")
                L_expenses_m.append(H_rent_m)
                M_balance-=H_rent_m
                print("Your balance amount is",M_balance)
                P_bal.append((H_rent_m/Tot_income_m)*100)
            else:
                H_rent_m=0
            C_School = input("Do you pay children's school fees (Y/N):")
            if C_School in "yY":
                C_School_m = int(input("How much do you pay: "))
                L_expenses.append("Children\'s school fees ")
                L_expenses_m.append(C_School_m)
                M_balance -= C_School_m
                print("Your balance amount is", M_balance)
                P_bal.append((C_School_m / Tot_income_m) * 100)
            else:
                C_School_m = 0
            EWG = input("Do you pay charges for electricity,water and gas (Y/N):")
            if EWG in "yY":
                EWG_m = int(input("How much do you pay: "))
                L_expenses.append("Electricity,Water and gas charges")
                L_expenses_m.append(EWG_m)
                M_balance -= EWG_m
                print("Your balance amount is", M_balance)
                P_bal.append((EWG_m / Tot_income_m) * 100)
            else:
                EWG_m = 0
            Food = input("Do you pay for food (Y/N):")
            if Food in "yY":
                Food_m = int(input("How much do you pay: "))
                L_expenses.append("Food charges")
                L_expenses_m.append(Food_m)
                M_balance -= Food_m
                print("Your balance amount is", M_balance)
                P_bal.append((Food_m / Tot_income_m) * 100)
            else:
                Food_m = 0
            Tel = input("Do you pay charges for Telephone (Y/N):")
            if Tel in "yY":
                Tel_m = int(input("How much do you pay: "))
                L_expenses.append("Telephone")
                L_expenses_m.append(Tel_m)
                M_balance -= Tel_m
                print("Your balance amount is", M_balance)
                P_bal.append((Tel_m / Tot_income_m) * 100)
            else:
                Tel_m = 0
            Internet = input("Do you pay charges for Internet (Y/N):")
            if Internet in "yY":
                Internet_m = int(input("How much do you pay: "))
                L_expenses.append("Internet")
                L_expenses_m.append(Internet_m)
                M_balance -= Internet_m
                print("Your balance amount is", M_balance)
                P_bal.append((Internet_m / Tot_income_m) * 100)
            else:
                Internet_m = 0
            Loan = input("Do you have any loan (Y/N):")
            if Loan in "yY":
                qn_loan=input("Do you know the yearly interest amount?(Y/N)")
                if qn_loan in "Yy":
                    interest=float(input("Enter the interest amount you are paying per year:"))
                    Loan_m=interest
                elif qn_loan in "Nn":
                    SI = input("Do you want to find SI (Simple Interest)(Y/N):")
                    P = float(input("Enter the principle amount:"))
                    R = float(input("Enter rate of Interest(in%):"))
                    T = float(input("Enter the time period (in Years): "))
                    interest_SI = (P * R * T) / 100
                    interest_CI = P * ((1 + (R / 100)) ** T)
                    time.sleep(1.5)
                    if SI == "Y" or SI == "y":
                        interest=interest_SI
                        print("The Simple interest amount is", interest)
                        time.sleep(1)
                        Loan_m = (P + interest) / T
                    elif SI == 'n' or SI == "N":
                        print("The Compound interest amount is", interest_CI)
                        interest=interest_CI-P
                        time.sleep(1)
                        Loan_m = (P+interest)/T
                L_expenses.append("Loan")
                L_expenses_m.append(Loan_m)
                M_balance -= Loan_m
                print("Your balance amount is", M_balance)
                P_bal.append((Loan_m / Tot_income_m) * 100)
            else:
                Loan_m = 0
            Maid = input("Do you pay for maid service (Y/N):")
            if Tel in "yY":
                Maid_m = int(input("How much do you pay(per month): "))
                L_expenses.append("Maid Charges")
                L_expenses_m.append(Maid_m*12)
                M_balance -= Maid_m*12
                print("Your balance amount is", M_balance)
                P_bal.append(((Maid_m*12) / Tot_income_m) * 100)
            else:
                Maid_m = 0
            Clothing = input("Do you pay yearly for clothing (Y/N):")
            if Clothing in "yY":
                Clothing_m = int(input("How much do you pay: "))
                L_expenses.append("Clothing")
                L_expenses_m.append(Clothing_m)
                M_balance -= Clothing_m
                print("Your balance amount is", M_balance)
                P_bal.append((Clothing_m / Tot_income_m) * 100)
            else:
                Clothing_m = 0
            Entertainment = input("Do you pay for entertainment yearly (Y/N):")
            if Entertainment in "yY":
                Entertainment_m = int(input("How much do you pay: "))
                L_expenses.append("Entertainment")
                L_expenses_m.append(Entertainment_m)
                M_balance -= Entertainment_m
                print("Your balance amount is", M_balance)
                P_bal.append((Entertainment_m / Tot_income_m) * 100)
            else:
                Entertainment_m = 0
            Vacation = input("Do you go for vacation yearly (Y/N):")
            if Vacation in "yY":
                Vacation_m = int(input("How much do you pay: "))
                L_expenses.append("Vacation")
                L_expenses_m.append(Vacation_m)
                M_balance -= Vacation_m
                print("Your balance amount is", M_balance)
                P_bal.append((Vacation_m / Tot_income_m) * 100)
            else:
                Vacation_m = 0
            Medical = input("Do you pay yearly for medical (Y/N):")
            if Medical in "yY":
                Medical_m = int(input("How much do you pay: "))
                L_expenses.append("Medical")
                L_expenses_m.append(Medical_m)
                M_balance -= Medical_m
                print("Your balance amount is", M_balance)
                P_bal.append((Medical_m / Tot_income_m) * 100)
            else:
                insurance=input("Do you pay for insurance(Y/N):")
                if insurance in "Yy":
                    insurance_m = int(input("How much do you pay: "))
                    L_expenses.append("Insurance")
                    L_expenses_m.append(insurance_m)
                    M_balance -= insurance_m
                    print("Your balance amount is", M_balance)
                    P_bal.append((insurance_m / Tot_income_m) * 100)
                else:
                    Medical_m = 0
            Visa = input("Do you have a residential visa (Y/N):")
            status= input("Are you an investor(Y/N):")
            if Visa in "yY":
                if status in "Yy":
                    Status = input("Are you a gold visa holder(Y/N)")
                    if Status in "Yy":
                        print("Thats cool!")
                        L_expenses.append("Visa")
                        L_expenses_m.append(120)
                        M_balance-=120
                        print("Your balance amount is",M_balance)
                        P_bal.append((120/Tot_income_m)*100)
                    else:
                        Visa_m = int(input("How much do you pay: "))
                        L_expenses.append("Visa")
                        L_expenses_m.append(Visa_m/3)
                        M_balance -= Visa_m/3
                        print("Your balance amount is", M_balance)
                        P_bal.append(((Visa_m/3) / Tot_income_m) * 100)
                else:
                    Visa_m = int(input("How much do you pay: "))
                    L_expenses.append("Visa")
                    L_expenses_m.append(Visa_m/2)
                    M_balance -= Visa_m/2
                    print("Your balance amount is", M_balance)
                    P_bal.append((Visa_m / Tot_income_m) * 100)
            else:
                Visa_m = 0
            Equities = input("Do you pay for Equities (Y/N):")
            if Equities in "yY":
                Equities_m = int(input("How much do you pay(per month): "))
                L_expenses.append("Equities")
                L_expenses_m.append(Equities_m * 12)
                M_balance -= Equities_m * 12
                print("Your balance amount is", M_balance)
                P_bal.append(((Equities_m * 12) / Tot_income_m) * 100)
            else:
                Equities_m = 0
            Travel = input("Do you travel (Y/N):")
            if Travel in "yY":
                Freq=int(input("How frequently do you travel?:"))
                Travel_m = int(input("How much do you pay per travel: "))
                L_expenses.append("Travel")
                L_expenses_m.append(Travel_m * Freq)
                M_balance -= Travel_m * Freq
                print("Your balance amount is", M_balance)
                P_bal.append(((Travel_m * Freq) / Tot_income_m) * 100)
            else:
                Travel_m = 0
            Furniture = input("Do you pay for Furniture (Y/N):")
            if Furniture in "yY":
                freq=int(input("How often do you buy furniture (No. of times per year):"))
                Furniture_m = int(input("How much do you pay per time:: "))
                L_expenses.append("Furniture")
                L_expenses_m.append(Furniture_m * freq)
                M_balance -= Furniture_m * freq
                print("Your balance amount is", M_balance)
                P_bal.append(((Furniture_m * freq) / Tot_income_m) * 100)
            else:
                Furniture_m = 0

            print("So your total number of ways of expenses are", len(L_expenses))
            print("i.e")
            for i in range(len(L_expenses)):
                print(L_expenses[i], end=",")
            T_expenses = sum(L_expenses_m)
            print("So your total expense is", T_expenses)
            save=T_expenses-T_income_m
            if save>0:
                print("You are saving",save*-1,"every year!")
            elif save==0:
                print("You are spending what you are earning every year!")
            else:
                print("You are spending more than that of you are earning!")

        elif term in "Mm":
            print("So you choose to select monthly report ")
            salary = int(input("What is your monthly salary:"))
            L_income_m.append(salary)
            overtime = input("Do you get paid for overtime(Y/N):")
            if overtime in "yY":
                overtime_m = int(input("How much are you paid for overtime per hour: "))
                freq = int(input("How many hours do you get overtime per month:"))
                L_income.append("Overtime")
                L_income_m.append(overtime_m * freq)
            else:
                overtime_m = 0
            Bonus = input("Do you get bonus monthly (Y/N):")
            if Bonus in "yY":
                Bonus_m = int(input("How much are you paid monthly in Bonus: "))
                L_income.append("Bonus")
                L_income_m.append(Bonus_m)
            else:
                Bonus_m = 0
            Other_benefits = input("Do you have any other medium of getting paid (Y/N) ? :")
            if Other_benefits in "Yy":
                n_benefits = int(input("How many other ways?:"))
                for i in range(n_benefits):
                    L_income.append(input("Enter the way:"))
                    L_income_m.append(int(input("Enter the amount:")))
            print("So your total number of ways of earning is", len(L_income))
            print("i.e")
            for i in range(len(L_income)):
                print(L_income[i], end=",")
            T_income_m = sum(L_income_m)
            print("So your total yearly income is", T_income_m)
            Tot_income_m = T_income_m
            M_balance = T_income_m

            # Expense
            H_rent = input("Do you have a rented home(Y/N):")
            if H_rent in "yY":
                H_rent_m = int(input("How much do you pay for home rent yearly: "))
                L_expenses.append("Home rent")
                L_expenses_m.append(H_rent_m/12)
                M_balance -= H_rent_m/12
                print("Your balance amount is", M_balance)
                P_bal.append((H_rent_m / Tot_income_m) * 100)
            else:
                H_rent_m = 0
            C_School = input("Do you pay children's school fees (Y/N):")
            if C_School in "yY":
                C_School_m = int(input("How much do you pay: "))
                L_expenses.append("Children\'s school fees ")
                L_expenses_m.append(C_School_m)
                M_balance -= C_School_m
                print("Your balance amount is", M_balance)
                P_bal.append((C_School_m / Tot_income_m) * 100)
            else:
                C_School_m = 0
            EWG = input("Do you pay charges for electricity,water and gas (Y/N):")
            if EWG in "yY":
                EWG_m = int(input("How much do you pay: "))
                L_expenses.append("Electricity,Water and gas charges")
                L_expenses_m.append(EWG_m)
                M_balance -= EWG_m
                print("Your balance amount is", M_balance)
                P_bal.append((EWG_m / Tot_income_m) * 100)
            else:
                EWG_m = 0
            Food = input("Do you pay for food (Y/N):")
            if Food in "yY":
                Food_m = int(input("How much do you pay: "))
                L_expenses.append("Food charges")
                L_expenses_m.append(Food_m)
                M_balance -= Food_m
                print("Your balance amount is", M_balance)
                P_bal.append((Food_m / Tot_income_m) * 100)
            else:
                Food_m = 0
            Tel = input("Do you pay charges for Telephone (Y/N):")
            if Tel in "yY":
                Tel_m = int(input("How much do you pay: "))
                L_expenses.append("Telephone")
                L_expenses_m.append(Tel_m)
                M_balance -= Tel_m
                print("Your balance amount is", M_balance)
                P_bal.append((Tel_m / Tot_income_m) * 100)
            else:
                Tel_m = 0
            Internet = input("Do you pay charges Internet (Y/N):")
            if Internet in "yY":
                Internet_m = int(input("How much do you pay: "))
                L_expenses.append("Internet")
                L_expenses_m.append(Internet_m)
                M_balance -= Internet_m
                print("Your balance amount is", M_balance)
                P_bal.append((Internet_m / Tot_income_m) * 100)
            else:
                Internet_m = 0
            Loan = input("Do you have any loan (Y/N):")
            if Loan in "yY":
                qn_loan = input("Do you know the yearly interest amount?(Y/N)")
                if qn_loan in "Yy":
                    interest=float(input("Enter the interest amount you are paying per month:"))
                    Loan_m=interest
                elif qn_loan in "Nn":
                    SI = input("Do you want to find SI (Simple Interest)(Y/N):")
                    P = float(input("Enter the principle amount:"))
                    R = float(input("Enter rate of Interest(in%):"))
                    T = float(input("Enter the time period (in Years): "))
                    interest_SI = (P * R * T) / 100
                    interest_CI = P * ((1 + (R / 100)) ** T)
                    time.sleep(1.5)
                    if SI == "Y" or SI == "y":
                        interest = interest_SI
                        print("The Simple interest amount is", interest)
                        time.sleep(1)
                        Loan_m = (P + interest) / T
                    elif SI == 'n' or SI == "N":
                        print("The Compound interest amount is", interest_CI)
                        interest = interest_CI - P
                        time.sleep(1)
                        Loan_m = (P + interest) / T
                L_expenses.append("Loan")
                L_expenses_m.append(Loan_m/12)
                M_balance -= Loan_m/12
                print("Your balance amount is", M_balance)
                P_bal.append(((Loan_m/12 )/ Tot_income_m) * 100)
            else:
                Loan_m = 0
            Maid = input("Do you pay for maid service (Y/N):")
            if Tel in "yY":
                Maid_m = int(input("How much do you pay(per month): "))
                L_expenses.append("Maid Charges")
                L_expenses_m.append(Maid_m)
                M_balance -= Maid_m
                print("Your balance amount is", M_balance)
                P_bal.append(((Maid_m) / Tot_income_m) * 100)
            else:
                Maid_m = 0
            Clothing = input("Do you pay monthly for clothing (Y/N):")
            if Clothing in "yY":
                Clothing_m = int(input("How much do you pay: "))
                L_expenses.append("Clothing")
                L_expenses_m.append(Clothing_m)
                M_balance -= Clothing_m
                print("Your balance amount is", M_balance)
                P_bal.append((Clothing_m / Tot_income_m) * 100)
            else:
                Clothing_m = 0
            Entertainment = input("Do you pay for entertainment monthly (Y/N):")
            if Entertainment in "yY":
                Entertainment_m = int(input("How much do you pay: "))
                L_expenses.append("Entertainment")
                L_expenses_m.append(Entertainment_m)
                M_balance -= Entertainment_m
                print("Your balance amount is", M_balance)
                P_bal.append((Entertainment_m / Tot_income_m) * 100)
            else:
                Entertainment_m = 0
            Vacation = input("Do you go for vacation monthly (Y/N):")
            if Vacation in "yY":
                Vacation_m = int(input("How much do you pay: "))
                L_expenses.append("Vacation")
                L_expenses_m.append(Vacation_m)
                M_balance -= Vacation_m
                print("Your balance amount is", M_balance)
                P_bal.append((Vacation_m / Tot_income_m) * 100)
            else:
                Vacation_m = 0
            Medical = input("Do you pay monthly for medical (Y/N):")
            if Medical in "yY":
                Medical_m = int(input("How much do you pay: "))
                L_expenses.append("Medical")
                L_expenses_m.append(Medical_m)
                M_balance -= Medical_m
                print("Your balance amount is", M_balance)
                P_bal.append((Medical_m / Tot_income_m) * 100)
            else:
                insurance = input("Do you pay for insurance(Y/N):")
                if insurance in "Yy":
                    insurance_m = int(input("How much do you pay: "))
                    L_expenses.append("Insurance")
                    L_expenses_m.append(insurance_m)
                    M_balance -= insurance_m
                    print("Your balance amount is", M_balance)
                    P_bal.append((insurance_m / Tot_income_m) * 100)
                else:
                    Medical_m = 0
            Visa = input("Do you have a residential visa (Y/N):")
            status = input("Are you an investor(Y/N):")
            if Visa in "yY":
                if status in "Yy":
                    Status = input("Are you a gold visa holder(Y/N)")
                    if Status in "Yy":
                        print("Thats cool!")
                        L_expenses.append("Visa")
                        L_expenses_m.append(10)
                        M_balance -= 10
                        print("Your balance amount is", M_balance)
                        P_bal.append((10 / Tot_income_m) * 100)
                    else:
                        Visa_m = int(input("How much do you pay: "))
                        L_expenses.append("Visa")
                        L_expenses_m.append(Visa_m / 36)
                        M_balance -= Visa_m / 36
                        print("Your balance amount is", M_balance)
                        P_bal.append(((Visa_m / 36) / Tot_income_m) * 100)
                else:
                    Visa_m = int(input("How much do you pay: "))
                    L_expenses.append("Visa")
                    L_expenses_m.append(Visa_m / 24)
                    M_balance -= Visa_m / 24
                    print("Your balance amount is", M_balance)
                    P_bal.append((Visa_m / Tot_income_m) * 100)
            else:
                Visa_m = 0
            Equities = input("Do you pay for Equities (Y/N):")
            if Equities in "yY":
                Equities_m = int(input("How much do you pay(per month): "))
                L_expenses.append("Equities")
                L_expenses_m.append(Equities_m)
                M_balance -= Equities_m
                print("Your balance amount is", M_balance)
                P_bal.append(((Equities_m) / Tot_income_m) * 100)
            else:
                Equities_m = 0
            Travel = input("Do you travel yearly (Y/N):")
            if Travel in "yY":
                Freq = int(input("How many times do you travel in one year?:"))
                Travel_m = int(input("How much do you pay per travel: "))
                L_expenses.append("Travel")
                L_expenses_m.append(Travel_m * Freq/12)
                M_balance -= Travel_m * Freq/12
                print("Your balance amount is", M_balance)
                P_bal.append(((Travel_m * Freq/12) / Tot_income_m) * 100)
            else:
                Travel_m = 0
            Furniture = input("Do you pay for Furniture yearly (Y/N):")
            if Furniture in "yY":
                freq = int(input("How often do you buy furniture (No. of times per month):"))
                Furniture_m = int(input("How much do you pay per time on average: "))
                L_expenses.append("Furniture")
                L_expenses_m.append(Furniture_m * freq/12)
                M_balance -= Furniture_m * freq/12
                print("Your balance amount is", M_balance)
                P_bal.append(((Furniture_m * freq/12) / Tot_income_m) * 100)
            else:
                Furniture_m = 0

            print("So your total number of ways of expenses are", len(L_expenses))
            print("i.e")
            for i in range(len(L_expenses)):
                print(L_expenses[i], end=",")
            T_expenses = sum(L_expenses_m)
            print("So your total expense is", T_expenses)
        graph=input("Do you want to see the expense graph ")
        y=L_expenses_m
        length=len(L_expenses_m)
        x=[]
        j=0
        for i in range(length):
            j+=2
            x.append(j)
        plt.bar(x,y),time.sleep(1)
        plt.show()
    elif sel == 5:
        str1 = ''
        first = True
        CONTINUE = 'Y'
        if first == True:
            val1 = int(input('Enter no : '))
            str1 = str(val1)
        while CONTINUE in 'Yy':
            op = input('Enter operator : ')
            val2 = int(input('Enter no : '))
            if op == '+':
                result = val1 + val2
            elif op == '-':
                result = val1 - val2
            elif op == '*':
                result = val1 * val2
            elif op == '/':
                result = val1 / val2
            else:
                print('Wrong Operator !!!')
                break
            first = False
            val1 = result
            str1 = str1 + op + str(val2)
            CONTINUE = input('Do you want to continue (Y/N)?  ')

        print('\n =====================\n')
        print(str1, ' = ', result)
        print('\n =====================\n')
    C=input("Do you want to continue runnning the program for another task (Y/N):")
print('''Thank You for Staying up till now
with your uttermost patience. 
Thank you and have a nice day 😀!''')
print('''If you are reading this
then it is due to support from
1)      My parents and lil bro 🥳
2)      Jihan Ma\'am 👩‍🏫
3)      My friends 🎭''')
time.sleep(1)
print('''A project by
                       𝔄𝒷𝒾𝓃𝓇𝒶𝒿  ℬ𝓱𝒶𝓈𝓀𝒶𝕣ᴬ𝔫 𝕯.
                       𝟙𝟙 𝛅
                       0𝟜''')
time.sleep(1.5)
y="Y"
while y in "Y":
    def draw_circle(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()


    def draw_triangle(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(size * 3)
            turtle.left(120)
        turtle.end_fill()
        turtle.setheading(0)


    def draw_square(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size * 2)
            turtle.left(90)
        turtle.end_fill()
        turtle.setheading(0)


    def draw_star(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(144)
        for i in range(5):
            turtle.forward(size * 2)
            turtle.right(144)
            turtle.forward(size * 2)
        turtle.end_fill()
        turtle.setheading(0)

    # Create a turtle named Tommy:
    tommy = Turtle()
    tommy.shape("turtle")
    tommy.speed(7)

    # Draw three circles:
    draw_circle(tommy, "green", 50, 15, 40)
    draw_square(tommy, "blue", 50, 40, 0)
    draw_star(tommy, "yellow", 50, -25, 0)
    draw_triangle(tommy, "navy", 50, -25, 0)
    draw_star(tommy, "yellow", 5, 125, 0)
    draw_star(tommy, "brown", 5, -125, 0)
    draw_star(tommy, "red", 5, -125, 100)

    # Write a little message:
    tommy.penup()
    tommy.goto(0, -50)
    tommy.color("black")
    tommy.write("Crazy Calculator", False ,'center', ("Cambria",24,"bold"))
    tommy.goto(0, -80)
    time.sleep(1)
    y="y"
    quit()