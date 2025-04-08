def str(text):
    voewls="aeiouAEIOU"
    const=[]
    for char in text:
        if char.isalpha() and char not in voewls:
            const.append(char)
            
    if len(const)<3:
        return "not"
    return  const[-3]

text="hello world"
print(str(text))
            
            
def str(text):
    voews='aeiouAEIOU'
    conat=[]
    for char in text:
        if char.isalpha() and char not in voews:
            conat.append(char)
    if len(conat)<3:
        return 'not'
    return conat[-3]

text='hello world'

print(str(text))
    
    

a=int(input("entrt"))
res=1
for i in range(1,a+1):
    res=res*i
    
print(res)

b=int(input("entrt"))
sum=0
for i in range(1,b+1):
    if   b % i ==0:
         sum=sum+i
print(sum)

# c="abcdsd"
# d=c.sorted()

# print(d)   


a=[5,2,3,6,1,4,8]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            
print(a)



a="rama is rama and "
b=""
c=a.split()
for char in c:
    if char not in b:
        b=b+char+' '
print(b)


a=1,5,3,2,6
b=sorted(a)
for i in b:
    sum=b[len(b)-1] + b[len(b)-2]
print(b)
print(sum)

