with open("Input/numbers.txt", "r+") as file:
    result = file.readlines()
    result_max = max(result ,key=lambda x: x)
    
with open("Ouput/output03.txt","w") as file02:
    file02.write(str(result_max))