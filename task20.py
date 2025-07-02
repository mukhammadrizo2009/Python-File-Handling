with open("Input/grades.csv","r+") as file:
    reading = file.readlines()[1:]
    
    result01 = []
    
    for i in reading:
       parts = i.strip().split(",")
       result01.append(int(parts[1]))
       
    total = sum(result01)
    result = total / (len(result01))
    
with open("Ouput/output20.txt", "w+") as file02:
   file02.write(str(result))
    
    

