medical_card=input("do u have madical card y or n")
attendence=int(input("what is your attendence"))
if medical_card=='y':
 print("allowed")
else:
  if attendence >=75:
    print("allowed")
  else:
    print("not allowed")  


unit=int(input("plz enter the units u have consumed"))
if (unit<50) :
  amount = unit*2.60
  surcharge=25
elif (unit<=100):
  amount= 130+ ((unit - 50)*3.25)
  surcharge=25
elif (unit<=200):
  amount=130+162.50 + ((unit-100)*5.26)
  surcharge=45
else:
  amount=130+ 162.50+526((unit-200)*8.45)
  surcharge=75
total=amount+surcharge
print("\n electrcity bill = %.2f" %total)



     

     
