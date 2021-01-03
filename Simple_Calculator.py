import time

Y="y"
print('''First of all Thank you for choosing this option
            Here you will be provided with option to choose for the mathematical operations
             You just have to answer it according to your needs to get the right output
             So lets open up our Text_based Calculator......''')
time.sleep(1.5)
calcu=int(input("For Simple Calculator enter \"1\" or enter \"2\" for for Complex calculator:"))
n_num=int(input("Enter the number of entries you want to make:"))
L_num=[]
L_sym=[]
result=0
result_m=1
if calcu==1:
    for i in range(n_num-1):
        num=int(input("Enter the number:"))
        L_num.append(num)
        print("1 for Add,  2 for Subtraction,  3 for multiplication,  4 for division")
        print('''For simplicity if your keyboard is having all the keys working fine then
                pressing + for Add,  - for Subtraction, * for multiplication and / for division is also fine''')
        symbol=input("Enter the symbol:")
        L_sym.append(symbol)
    num = int(input("Enter the number:"))
    L_num.append(num)
    for i in range(n_num-1):
        if L_sym[i] in "/4":
            result = L_num[i] / L_num[i + 1]
        elif L_sym[i] in "*3":
            result=L_num[i]*L_num[i+1]
        elif L_sym[i] in "+1":
            result=L_num[i]+L_num[i+1]
        elif L_sym[i] in "-2":
            result = L_num[i]-L_num[i+1]
    print("So what you ment to calculate is",)
    for i in range(n_num):
        print(L_num[i],L_sym[i],end="")
        print("=",result)

