list = ["apple", "banana", "apple","ornage", "mango"]
for i in list:
    if(list.count(i)>1):
        duplicate = i
        break
print(f"{duplicate} is the duplicate that is not unique")