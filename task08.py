with open("Input/numbers.txt" , "r+") as file:
    nums = file.readlines()
    
numbers = [] 
  
for i in nums:
    result = int(i)
    if result % 5 == 0:
            numbers.append("".join(i))
            
with open("Ouput/output08.txt","w") as file02:
    file02.write(str(numbers))