#num =int(input("Enter the number"))
#fact =1
#for i in range(1,num+1):
 #   fact*=i
#print(fact) 


num =int(input("Enter the number"))
fact =1
while(num>0):
    fact*=num
    num-=1
print(fact) 