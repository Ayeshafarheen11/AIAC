f = open("example.txt","r")
nums = f.readlines()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

f2 = open("square.txt","w")
for sq in squares:
    f2.write(str(sq) + "\n")

print("Square written")
f.close()
f2.close()
