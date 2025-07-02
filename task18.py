
ism = input("ism kiriting!: ").title()

with open("Input/students.txt") as file:
    students = file.read()
    
    if ism in students:
        natija = f"{ism} ismi mavjud."
    else:
        natija = f"{ism} ismi mavjud emas"
        
with open("Ouput/output18.txt","w") as file02:
    file02.write(f"{natija}")
