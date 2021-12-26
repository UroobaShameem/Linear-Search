list= [2,4,6,8,12]
n=int(input("Enter number you want to search: "))
for i in range(len(list)):
   if list[i]==n:
       print("Number found")
       break
else:
       print("Number not found") 