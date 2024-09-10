#LIST-INDEX UNIQUE
#TUPLE-INDEX UNIQUE
#SET-ITEM UNIQUE
#DICTIONARY-KEY UNIQUE


#DICTIONARY-dict{}
#key value pair
#key:value,
#duplicates key are not allowed
#ordered
#keys(),values(),items()


mark={}
print(type(mark))#<class 'dict'>


phone_numbers={
    "akshay":987,
    "sarath":123,
    "akhil":456
}

print(phone_numbers)#{'akshay': 987, 'sarath': 123, 'akhil': 456}

print(phone_numbers['akshay'])#987

phone_numbers['akshay']=888
print(phone_numbers)#{'akshay': 888, 'sarath': 123, 'akhil': 456}


print(phone_numbers.get("sarath"))#123

phone_numbers.update({"sarath":999})
print(phone_numbers)#{'akshay': 987, 'sarath': 999, 'akhil': 456}


phone_numbers["hafeed"]=555
print(phone_numbers)#{'akshay': 987, 'sarath': 123, 'akhil': 456, 'hafeed': 555}

phone_numbers.update({"benison":755})
print(phone_numbers)#{'akshay': 987, 'sarath': 123, 'akhil': 456, 'hafeed': 555, 'benison': 755}

phone_numbers.clear()
print(phone_numbers)#{}



del phone_numbers['sarath']
print(phone_numbers)#{'akshay': 987, 'akhil': 456}

del phone_numbers
print(phone_numbers)



num={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}
num["e"]=5
print(num)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



roll_numbers={
    1:"anand",
    2:"benison",
    3:"hafeed",
}

#pop
roll_numbers.pop(2)#2-key
print(roll_numbers)#{1: 'anand', 3: 'hafeed'}

#popitem()
roll_numbers.popitem()
print(roll_numbers)#{1: 'anand'}

#clear
roll_numbers.clear()
print(roll_numbers)#{}

print(roll_numbers.keys())#dict_keys([1, 2, 3])
print(roll_numbers.values())#dict_values(['anand', 'benison', 'hafeed'])
print(roll_numbers.items())#dict_items([(1, 'anand'), (2, 'benison'), (3, 'hafeed')])


for i in roll_numbers:
    print(i)#1
            #2
            #3


for i in roll_numbers:
    print(roll_numbers[i])#anand
                          #benison
                          #hafeed
    


for i in roll_numbers.keys():
    print(i)#1
            #2
            #3
    
 
for i in roll_numbers.values():
    print(i)#anand
            #benison
            #hafeed
    
for i in roll_numbers.items():
    print(i)#(1, 'anand')
            #(2, 'benison')
            #(3, 'hafeed')
    

for i,j in roll_numbers.items():
    print(i,j)#1 anand
             #2 benison
             #3 hafeed






subjects=[]
marks=[]
for i in range(3):
    sub=input("Enter your subject name:")
    mark=int(input("Enter your mark:"))
    subjects.append(sub)
    marks.append(mark)
print(subjects)#['physics', 'maths', 'biology']
print(marks)#[35, 45, 50]



#ZIP()
#used to combine two or more list,tuple,dict etc.

subjects=["physics","maths","biology"]
marks=[35,45,50] 

mark_sheet=dict(zip(subjects,marks))
print(mark_sheet)#{'physics': 35, 'maths': 45, 'biology': 50}

mark_sheet=list(zip(subjects,marks))
print(mark_sheet)#[('physics', 35), ('maths', 45), ('biology', 50)]



A+ 91-100
A 81-90
B+ 71-80
B  61-70
C 51-60
D 41-50
F BELOW 40

students_marks={
    "anand":92,
    "akhil":84,
    "benison":74,
    "cenoy":64,
    "hafeed":55,
    "jithin":42,
    "nithn":28,
}

students_grade={}
for name in students_marks:
    mark=students_marks[name]
    #mark=student_marks.get(name)
    if mark>90:
        students_marks[name]="A+"
        #students_grades.update({name}:"A+")
    elif mark>80:
        students_marks[name]="A"
    elif mark>70:
        students_marks[name]="B+"
    elif mark>60:
        students_marks[name]="B"
    elif mark>50:
        students_marks[name]="C+"
    elif mark>40:
        students_marks[name]="D"
    else:
        students_marks[name]="F"
print(students_marks)#{'anand': 'A+', 'akhil': 'A', 'benison': 'B+', 'cenoy': 'B', 'hafeed': 'C+', 'jithin': 'D', 'nithn': 'F'}   


'''
x={"a":10,"b":20,"c":30}






    
