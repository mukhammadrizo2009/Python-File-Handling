with open("Input/numbers.txt", "r+") as file:
    result = file.readlines()
    
    result1 = result.split()
    
    result_max = max(result1 , key=int)
    
with open("Ouput/output03.txt","w") as file02:
    file02.write(str(result_max))