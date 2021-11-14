def three_numbers():
    n1= int(input("1st number:"))
    n2= int(input("2nd number:"))
    n3= int(input("3rd number:"))
    return n1,n2,n3

number1,number2,number3= three_numbers()

min = number1
if number2<min:
    print("Number 2 is the smallest number")
    min=number2
else:
    if number3<min:
        print("Number 3 is the smallest number")
        min=number3
    else:
        print("Number 1 is the smallest number")
