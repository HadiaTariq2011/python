print("half pettern pyramid of star(*)")
n=int(input("enter the NUMBER OF ROWS"))
for i in range(n):
    for j in range(i+1):
      print("*",end="")
    print()




rows=int(input("enter total number of rows:" ))
number=1
print("Floyd triangle")
for i in range(1,rows+1):
 for j in range(1,i+1):
   print(number,end=' ')
   number=number+1
 print()

