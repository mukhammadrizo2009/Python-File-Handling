with open("Input/grades.csv","r+") as file:
    reading = file.read()
    
with open("Ouput/output19.txt", "w+") as file02:
    file02.write(reading)