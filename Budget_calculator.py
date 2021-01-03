from matplotlib import pyplot as plt
import time
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
        qn_loan=input("Do you know the yearly interest amount?(Y/N)")
        if qn_loan in "Nn":
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
        print("You are saving",save,"every year!")
    elif save>0:
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
        if qn_loan in "Nn":
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
y=L_expenses_m
length=len(L_expenses_m)
x=[]
j=0
for i in range(length):
    j+=2
    x.append(j)
plt.bar(x,y),time.sleep(1)
plt.show()

