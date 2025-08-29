data = open("example.txt","r").readlines()
output = open("output.txt","w")

for line in data:
    output.write(line.upper())

print("processing done ")

output.close()


