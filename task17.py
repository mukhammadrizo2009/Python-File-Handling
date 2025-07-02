with open("Input/students.txt","r+") as file:
    names = file.readlines()
    
    result = filter(lambda name: name.lower().startswith("a"), names)
    
with open("Ouput/output17.txt" , "w") as file02:
    file02.writelines(result)