with open("Input/numbers.txt", "r+") as file:
    numbers = file.readlines()
    
    result = []
    
    for number in numbers:
        r = int(number) ** 2
        result.append(r)
        
    #print(result)
    
with open("Ouput/output07.txt","w") as file02:
    file02.write(str(result))