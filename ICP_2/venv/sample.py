x = input("enter the letter")
def letter(str):
    if(str=="p"):
        str="";
        for row in range(0,7):
            for column in range(0,7):
                if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or (
                        (column == 5 or column == 1) and (row == 1 or row == 2))):
                    str = str + "*"
                else:
                    str=str+" "
            str=str+"\n"
        print(str);
    else:
        print("enter vlaid letter")
letter(x)
