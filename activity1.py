tuplex=("tuple",False,3.2,1)
print(tuplex)
tuplex=(1,2,3,4,5,6,7)
print(tuplex)
tuplex=tuplex+(9,)
print(tuplex)
tuplex=(1,2,3,4,7,8,9,6)
_slice=tuplex[3:5]
print(_slice)
_slice=tuplex[:6]
print(_slice)



def palind(r):
    e = len(r)-1
    s=0
    while s<e:
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
        return True
r= (1,2,3,3,2,1)
if(palind(r)):
    print("tuple is flip flop")
else:
    print("not flip flop")


weather=(1,0,0,1,0,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if (weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if (sunny>rainy):
        print("good weather")
else:
        print("bad weather")    
        


