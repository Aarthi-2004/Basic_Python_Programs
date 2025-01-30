# write the program to print the grade of the marks

Marks = int(input("Enter the Scored marks:"))
if(Marks>=90):
    print("Grade A")
elif(Marks<=89 and Marks>=80):
    print("Grade B")
elif(Marks<=79 and Marks>=70):
    print("Grade C")
elif(Marks<=69 and Marks>=60):
    print("Grade D")
else:
    print("Failed")
