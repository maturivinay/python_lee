class employee:
    employ_count = 0
    salary_count=0
    def __init__(self, x, y, a, b): # __init__ default constructor
        self.x = x
        self.y = y #here the self is used to point out the variables in the constructot
        self.a = a
        self.b = b

        avg = self.a/self.b
        print(self.x,"'s age is", self.y)
        print("the average is ",avg)
        employee.employ_count +=1
        employee.salary_count=employee.salary_count + self.a
obj = employee("vinay", 20, 60000, 12)
obj = employee("rahul", 20, 120000, 12)
print( "Average is",employee.salary_count/employee.employ_count)


