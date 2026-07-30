str = str(input("Enter a string \n"))
for char in str:
    if str.count(char)==1:
        print(char)
        break