student_data={'id1':
             {'name':['Sara'],
              'CLASS':['V'],
              'subject_intergeration':['english,math,science']
             },
             'id2':
             {'name':['David'],
              'class':['V'],
               'subject_intergeration':['english,math,science']
              },
              'id3':
             {'name':['Surya'],
              'class':['V'],
               'subject_intergeration':['english,math,science']
              },
              'id4':
             {'name':['Sara'],
              'class':['V'],
               'subject_intergeration':['english,math,science']
              },
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)



test_dict={'codingal':2,'is':2,'best':2,'for':2,'coding':1}
print("the original dictionary:"+str(test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print("frequancy of K is :"+str(res))


country_code={'india':'0091',
              'Australia':'0025',
              'pakistan':'00977'}
print("country code for india-")
print(country_code.get('india','not found'))
print("country code for japan-")
print(country_code.get('japan','not found'))


