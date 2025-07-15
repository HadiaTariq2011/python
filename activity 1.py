my_set={1,2,3}
print(my_set)
my_set={1.0,"hello",(1,2,3)}
print(my_set)
my_set={1,2,3,4,3,2}
print(my_set)
my_set=set([1,2,3,2])
print(my_set,"\n")
num_set=set([0,1,2,3,4,5])
print("orignal set")
print(num_set)
num_set.pop()
print("after remiving the first element from the said set:")
print(num_set,"\n")


setx={"green","blue"}
sety={"blue","yellow"}
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz=setx.intersection(sety)
print(setz)



import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("orignal array:"+str(array_num))
print("Number of occurences of the number 3 in the said array"+str(array_num.count(3)))
array_num.reverse()
print("reverse the order of items")
print(str(array_num))