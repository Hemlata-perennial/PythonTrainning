#lambda usecases SYNTAX: lambda args:expr
x=lambda a: a*a
print(x(5))

#best used within higher order function
def new_func(x):
        return(lambda y: x+y)

t=new_func(5)
u=new_func(8)
print(t(6))
print(u(6))

#Filter(), reduce() and map()
mylist=[1,2,3,4,5,6]
res=list(filter(lambda a:(a%2==0),mylist)) #filter even numbers
print("lambda with filter:",res)
res=list(map(lambda a:(a%2==0),mylist)) #map with lambda 
print("lambda with Map:",res)
from functools import reduce
print("lambda with reduce",reduce(lambda a,b:a+b,[23,56,89,12,465,76]))

#Lambda for algebra
#for linear eq= 3X+4Y
s=lambda x,y:3*x+4*y
print("linear eq:",s(5,6))

#for quadratic eq: x^2+y^2
q=lambda x,y: (x**2)+(y**2)
print("quadratic eq:",q(5,6))