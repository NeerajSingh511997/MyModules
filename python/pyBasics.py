### Getting started with python 3 format;
# name = input("Hi, Whats's You Name: ");
# print(f"Good Morning, {name}");
# country = input("Which country do you belong: ");
# print(f"You live in {country}");
# likes = input("What would you like most between Cricket & Hockey: ");
# if name == "Cricket" : print(f"{likes} is the most popular in india");
# else : print(f"I like " + likes + " too");

### Checking behaviour of print statement;
# x = y = z = 50
# result = 50
# print ("name", result)
# print (result)
# print ("x = ", x)
# print ("y = " + y)
# print ("z = " + z)

### Assigning single values to multiple variables;
# x=y=z=50  
# print x
# print y  
# print z  

### Assigning multiple values to multiple variables;
# a,b,c=5,10,15
# print (a)
# print (b) 
# print (c)

### Exploring multiple assignments;
# first, middle, last = "Neeraj", "Singh", "Junior"
# print (first, middle, last)

student = {}
subjects = []
roll = None   
temp = None
print("Welcome to Student Maintenance System ...")
for x in range(0, 2):
    roll = input("Student %d Roll No: " %(x+1))
    count = int(input("Total No Of Subjects: "))
    tempList = []
    for y in range(0, count):
        temp = input("Subject %d: " %(y+1)) 
        tempList.append(temp)
    subjects.append(tempList)
    print(subjects)
    student[roll] = subjects[x]