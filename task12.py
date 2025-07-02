with open("Input/students.txt","r+") as file:
    reading = file.read()
    distance = list(reading)
    result = (len(distance))
    
with open("Ouput/output12.txt", "w+") as file02:
    file02.write(str(result))