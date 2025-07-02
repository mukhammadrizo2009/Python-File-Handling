with open("Input/grades.csv","r+") as file:
    file.readline
    reading = file.readlines
    
    rows = list(map(
        lambda line: line.strip().split(",")[0],
        reading
    ))
    high = max(
        rows,
        key=lambda row:[1]
    )
with open("Ouput/output21.txt", "w+") as file02:
   file02.write(str(high))