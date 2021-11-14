import math
grade= float(input("grade percentage:"))

if grade >= 96.5 and grade <=100:
    print("Grade/mark: 1.0")
    print("Description grade: excellent")
else:
    if grade >=93.5 and grade <=96.4:
        print("Grade/mark: 1.25")
        print("Description grade: excellent")
    else:
        if grade >=90.5 and grade <=93.4:
            print("Grade/mark: 1.75")
            print("Description grade: verygood")
        else:
            if grade >=87.5 and grade <=90.4:
                print("Grade/mark: 1.5")
                print("Description grade: verygood")
            else:
                if grade >=84.5 and grade <=87.4:
                    print("Grade/mark: 2.0")
                    print("Description grade: good")
                else:
                    if grade >=81.5 and grade <=84.4:
                        print("Grade/mark: 2.25")
                        print("Description grade: good")
                    else:
                        if grade >=78.5 and grade <=81.4:
                            print("Grade/mark: 2.5")
                            print("Description grade: satisfactory")
                        else:
                            if grade >=75.5 and grade <=78.4:
                                print("Grade/mark: 2.75")
                                print("Description grade: passing.")
                            else:
                                if grade >=74.5 and grade ==75.4:
                                    print("Grade/mark: 3.0")
                                    print("Description grade: passing.")
                                else:
                                    if grade >=64.5 and grade <=74.4:
                                        print("Grade/mark: 5.0")
                                        print("Description grade: failure.")
                                    else:
                                        print("Incomplete")
                                        print("Withdrawn")
                                        print("Dropped")