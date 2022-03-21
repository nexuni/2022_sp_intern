import string

# please reference https://www.trust.org.tw/upload/1100002250002.pdf
# or code in C++ https://cynthiachuang.github.io/Check-Tax-ID-Number/

def check_taiwan_tax_id(tax_id):
    """
    Input
        - tax_id: str
    Output
        - boolean
    """
    b=list()
    x=str(tax_id)
    c=list()
    N=0
    for i in x:
        b=b+[i]
    if len(b)!=8:
        return False
    else:
        weight_list = [1, 2, 1, 2, 1, 2, 4, 1]
        for i in range(len(weight_list)):
            c.append(int(b[i])*weight_list[i])
        


        for i in range(len(c)):
            c[i]=s(c[i])
        # print(c)
        


    #     n0=int(b[0])*1
    #     n1=int(b[1])*2
    #     n2=int(b[2])*1
    #     n3=int(b[3])*2
    #     n4=int(b[4])*1
    #     n5=int(b[5])*2
    #     n6=int(b[6])*4
    #     n7=int(b[7])*1
    #     N0=s(n0)
    #     N1=s(n1)
    #     N2=s(n2)
    #     N3=s(n3)
    #     N4=s(n4)
    #     N5=s(n5)
    #     N6=s(n6)
    #     N7=s(n7)

    ANS=0
    for i in range(len(c)):
        ANS=ANS+c[i]
    ANS=ANS-c[6]
    # print(ANS)


    if b[6]=="7":
        s1=special1(c[6])
        s2=special2(c[6])
        # print(s2)
        # print(s1)



        ANS=ANS+int(s1)
        # print(ANS)
        c1=check(ANS)
        # print("c1:", str(c1))

        if c1:
            return(True)
        else:
            ANS=ANS-int(s1)+int(s2)
            return(check(ANS))
    else:
        
        # for i in range(len(c)):
        #     ANS=ANS+c[i]
        ANS=ANS+c[6]
        return(check(ANS))


    # if b[6]==7:
    #     s1=special1(b[6])
    #     s2=special2(b[6])
    #     ANS=int(N0)+int(N1)+int(N2)+int(N3)+int(N4)+int(N5)+int(s1)+int(N7)
    #     c1=check(ANS)

    #     if c1==True:
    #         return(True)
    #     else:
    #         ANS=int(N0)+int(N1)+int(N2)+int(N3)+int(N4)+int(N5)+int(s2)+int(N7)
    #         return(check(ANS))
    # else:
    #     ANS=int(N0)+int(N1)+int(N2)+int(N3)+int(N4)+int(N5)+int(N6)+int(N7)
    #     return(check(ANS))


def s(x):
    a=list()
    b=0
    c=0
    x=str(x)
    for i in x:
        a=a+[i]

    c=len(a)
    for i in range(c):
        b+=int(a[i])
    return(b)

def special1(n):
    s1=int(n)//10
    return(s1)

def special2(n):
    s2=int(n)%10
    return(s2)

def check(x):
    if x%10==0:
        return True
    else:
        return False


# s(10)
# s(28)
# s(79)
# s(35)
# s(71)
# s(94)





# Test data
print(check_taiwan_tax_id("53619559"))
print(check_taiwan_tax_id("53619549"))
print(check_taiwan_tax_id("64387543"))
print(check_taiwan_tax_id("23328674"))
print(check_taiwan_tax_id("23328673"))
print(check_taiwan_tax_id("23673"))

