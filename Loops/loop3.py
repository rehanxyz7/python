print("GIVE A NUMBER \n")
v = int(input("Give the number \n"))

for i in range(1,11):
    if(i==5):
            continue 
    
    print(f"The multiplication of {v} with {i} is : {v*i}")
    if(i==5):
        continue 
