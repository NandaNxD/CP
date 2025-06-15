import shutil

fileName=input()

# C++

#files=['a.cpp','b.cpp','c.cpp','d.cpp','e.cpp','f.cpp']

# flag=0

# for file in files:
#     if(len(fileName)):
#         if(file[0]==fileName[0]):
#             flag=1
#             shutil.copy('./template','./'+file)


# if flag==0:
#     for file in files:
#         shutil.copy('./template','./'+file)


# Java

flag=0

files=['a.java','b.java','c.java','d.java','e.java','f.java']

for file in files:
    if(len(fileName)):
        if(file[0]==fileName[0]):
            flag=1
            shutil.copy('./java-templates/'+file[0],'./'+file)


if flag==0:
    for file in files:
        shutil.copy('./java-templates/'+file[0],'./'+file)
