with open("Input/grades.csv","r+") as file:
    reading = file.readlines()[1:]
    
    result01 = []
    
    for i in reading:
        if i == 5 :
            result01.append(i)
        
with open("Ouput/output22.txt", "w+") as file02:
   file02.write(str(result01))