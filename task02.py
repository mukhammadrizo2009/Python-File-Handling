with open("Input/numbers.txt", "r+") as file:
    result = file.read()
    
    result01 = [int(num) for num in result.split()]
    total = sum(result01)
with open("Ouput/output02.txt","w") as file02:
    file02.write(str(total))