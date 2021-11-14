
print("THE LIFE STAGES OF A PERSON")

age= int(input("Enter age:"))
if -1 < age <= 12:
    print('Kid')
elif 13 >= age <= 17:
    print('Teen')
elif age == 18:
    print('Debut')
else:
    print('Adult')