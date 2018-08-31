letters=["****", "*** ", " ***", "** *", "**  ", " ** ", "  **", "* * ", "*  *", " * *", "*   ", " *  ", "  * ", "   *"]
x=input("enter your name with First name")

def final_program(str):
    if(str=="C"):
        i=0;
        str=letters[0]+ "\n" +letters[10]+ "\n" +letters[10]+ "\n"+letters[10]+ "\n" + letters[0]
        print(str)
    elif(str=="A"):
        print("\n")
        str=letters[5]+ "\n" +letters[8] + "\n" +letters[8] +"\n" +letters[0]+"\n" +letters[8]+"\n" +letters[8]
        print(str)
    elif(str=="V"):
        str=letters[8]+ "\n" + letters[8] + "\n" + letters[12]
        print(str)
ab=x[0]
print(ab)
final_program(ab)

