



a=input("enter the first name")
b=input("enter the last name")
first=''.join(reversed(a))
last=''.join(reversed(b))
print(first,last)

c=int(input("enter number_1:"))
d=int(input("enter number_2:"))
print(c+d);

e=input("enter the string")
p=0
q=0
for x in e:
    if x.isalpha():
        p=p+1
    if x.isdigit():
        q=q+1
print("digits are", q)
print("digits are", p)



print(p)




