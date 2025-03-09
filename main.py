# Kerolos Amgad Coder

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divided(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divided
}
def calculator():
    should_accoumlator=True
    num_1=float(input("Enter Your First number :"))
    while should_accoumlator :
        for symbols in operations :
            print(symbols)
        symbol_operation=input("Enter the operation :")
        num_2=float(input ("Enter your second number :"))
        answer=operations[symbol_operation](num_1,num_2)
        print(f"{num_1} {symbol_operation} {num_2} ={answer}")
        choice=input(f"Do you want continue with this value {answer} type 'y' or "
                     f"you want to new calculation type 'n'").lower()
        if choice=="y":
            num_1=answer
        else:
            print("\n"*20)
            calculator()
calculator()