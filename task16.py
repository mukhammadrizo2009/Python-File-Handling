with open("Input/students.txt","r+") as file:
    names = file.readlines()
    
    result = []
    for name in names:
        if len(name) >= 5:
            result.append(name)
            
    #print(result)
    
with open("Ouput/output16.txt","w") as file02:
    file02.writelines(str(result))