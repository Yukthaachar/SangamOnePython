def perm3(input):
    list1=[]
    s1 = input[0]
    s2 = input[1]
    s3 = input[2]
    list1.append(s1+s2+s3)
    list1.append(s1+s3+s2)
    list1.append(s2+s1+s3)
    list1.append(s2+s3+s1)
    list1.append(s3+s1+s2)
    list1.append(s3+s2+s1)
    return list1
def perm4(input):
    list1=[]
    for j in range(0,4,1):
        s1 = input[j]
        s2 = input[0:j]+input[j+1:4]
        s3 = perm3(s2)
        for i in range(0,6,1):
            list1.append(s1+s3[i])
    return list1
def perm5(input):
    list1=[]
    for j in range(0, 5, 1):
        s1 =input[j]
        s2=input[0:j]+input[j+1:5]
        s3=perm4(s2)
        for i in range(0,24,1):
            list1.append(s1+s3[i])
    return list1
def perm6(input):
    list1=[]
    for j in range(0, 6, 1):
        s1 =input[j]
        s2=input[0:j]+input[j+1:6]
        s3=perm5(s2)
        for i in range(0,120,1):
            list1.append(s1+s3[i])
    return list1
def perm7(input):
    list1=[]
    for j in range(0, 7, 1):
        s1 =input[j]
        s2=input[0:j]+input[j+1:7]
        s3=perm6(s2)
        for i in range(0,720,1):
            list1.append(s1+s3[i])
    return list1
def perm8(input):
    list1=[]
    for j in range(0, 8, 1):
        s1 =input[j]
        s2=input[0:j]+input[j+1:8]
        s3=perm7(s2)
        for i in range(0,5040,1):
            list1.append(s1+s3[i])
    return list1
def perm9(input):
    list1=[]
    for j in range(0, 9, 1):
        s1 =input[j]
        s2=input[0:j]+input[j+1:9]
        s3=perm8(s2)
        for i in range(0,40320,1):
            list1.append(s1+s3[i])
    return list1

print("enter a word : ")
input1=input()
len1 = len(input1)
if len1==3:
    result=perm3(input1)
    print(result)
elif len1==4:
    result=perm4(input1)
    print(result)
elif len1==5:
    result=perm5(input1)
    print(result)
elif len1==6:
    result=perm6(input1)
    print(result)
elif len1==7:
    result=perm7(input1)
    print(result)
elif len1==8:
    result=perm8(input1)
    print(result)
elif len1==9:
    result=perm9(input1)
    print(result)
else:print("invalid input")