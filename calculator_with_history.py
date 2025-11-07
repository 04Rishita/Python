history_file="history.txt"

def show_history():
    file=open(history_file,'r')
    line=file.readlines()
    if len(line)==0:
        print("No History Found!")
    else :
        for line in reversed(line):
            print(line.strip())
    file.close()

def clear_history():
    file=open(history_file,'w')
    file.close()
    print("History Cleared")

def save(equation,result):
    file=open(history_file,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user):
    parts=user.split()
    if len(parts)!=3:
        print("Invalid input.")
        return
    
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    
    if op == "+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op == "/":
        result=num1/num2
    else:
        print("Invalid Operator")
        return
    if int(result)== result:
        result=int(result)
    print("Result:",result)
    save(user,result)


def main():
    print("---SIMPLE CALCULATOR (type history,clear,exit)")
    while True:
        user=input("enter calculation:")
        if user=="exit":
            break
        elif user=="history":
            show_history()
        elif user=="clear":
            clear_history()
        else:
            calculate(user)
main()

