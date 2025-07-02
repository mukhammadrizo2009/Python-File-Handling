with open("Input/students.txt","r+") as file:
    names = file.readlines()
    
    arr = []
    for name in names:
        newname = list(name)
        newname.reverse()
        arr.append("".join(newname))
        
    # print(arr)
    # print("".join(arr))
    
        


    

f2 = open("Ouput/output14.txt", "w")
f2.writelines(arr)