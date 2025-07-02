f = open("Input/students.txt","r+")

names = f.readlines()


result = sorted(names)

f2 = open("Ouput/output13.txt", "w")
f2.writelines(result)
