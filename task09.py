with open("Input/numbers.txt", "r+") as file:
    numbers = file.read().split('\n')
    
    result01 = []
    result02 = []
    result03 = []
    result04 = []
    
    for number in numbers:
        if len(number) == 1:
            result01.append("".join(number))
        elif len(number) == 2:
            result02.append("".join(number))
        elif len(number) == 3:
            result03.append("".join(number))
        elif len(number) >= 4:
            result04.append("".join(number))
            
    result = result01,result02,result03,result04
    
    with open("Ouput/output09.txt","w") as file02:
        file02.write(str(result))