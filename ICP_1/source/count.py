e=input("enter the string")
p=0
others=q=0

for x in e:
    if x.isalpha():
        p=p+1
    elif x.isdigit():
        q=q+1
    else:
        others=others+1;
print("digits are", q)
print("alphabets are", p)
print("others count is", others)
