with open("Input/numbers.txt", "r+") as file:
    numbers = file.read().split('\n')
    
    result = sorted(numbers)
    
with open("Ouput/sorted_number.txt","w") as file02:
    file02.write(str(result))
    
with open("Ouput/output10.txt","w") as file02:
    file02.write(str(result))