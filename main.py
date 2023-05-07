#substract numbers contained in a list 
def subtraction(numbers):
    
    for i in range(len(numbers)):
        if( numbers[i].isnumeric()): numbers[i] = int(numbers[i])
        else: numbers[i] = 0
    
    print("List of numbers: ", numbers)

    total=numbers[0]
    for i in range(1,len(numbers)):
        total = total - numbers[i]
    if (total>0):
        print("The result is positive.")
        return "POSITIVE"
    elif (total<0):
        print("The result is negative.")
        return "NEGATIVE"
    else: 
        print("The result is 0.")
        return "ZERO"



##main program
def main():
    while True:
        x = list(input("Enter multiple values: ").split())
        if (x == ["q"] or x==["Q"] or x==[]): break
        subtraction(x)
        ##print(addition(x))


main()
