n1= int(input("1st number:"))
n2= int(input("2nd number:"))
n3= int(input("3rd number:"))

smallest = 0

if n1 < n2 and n1 < n3:
    smallest = n1
else:
    if n2 < n3:
        smallest = n2
    else:
            smallest = n3
print(smallest, "is the smallest of three numbers.")
