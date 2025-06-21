def add(p,q):
    return p+q
def substract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please select the operation")
print("a.add")
print("b.substact")
print("c.multiply")
print("d.divide")
choice=input("enter your choice")
num_1=int(input("enter first number"))
num_2=int(input("enter second number"))
if choice =="a":
    print(num_1,"+", num_2, "=",add(num_1,num_2))
if choice =="b":
    print(num_1,"-", num_2, "=",substract(num_1,num_2))
if choice =="c":
    print(num_1,"*", num_2 ,"=",multiply(num_1,num_2))
if choice =="b":
    print(num_1,"/", num_2 ,"=",divide(num_1,num_2))    