tree1=23
tree2=56
tree3=45
tree4=65
tree5=87
sum = tree1+tree2+tree3+tree4+tree5 
print("sum of all five trees is", sum)
average=sum/5
print("the average is ",average)
Amount=int(input("plz enter amount"))
note_1 = Amount//100
note_2 =(Amount%100)//50
note_3 =((Amount%100)%50)//10
print("notes of 100 rs = ",note_1)
print("notes of 50 = ",note_2)
print("notes of 10 = ",note_3)
print("enter marks of subjects")
biology=int(input("biology:"))
physics=int(input("physics:"))
maths=int(input("maths:"))
urdu=int(input("urdu:"))
sum = biology+physics+maths+urdu
perc = (sum/400)*100
print("percentag is :",perc)