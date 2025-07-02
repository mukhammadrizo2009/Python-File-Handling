with open("Input/numbers.txt","r+") as file:
    reading = file.read()
    numbers = []
    for n in reading.split():
        if int(n) % 2 == 0:
            numbers.append(int(n))

            
with open("Ouput/output04.txt" , "w") as file02:
    file02.writelines(str(numbers))