import time

nums = [i for i in range(1,1000000)]# A list of numbers from 1 to 999999
squares = []
for n in nums:
    squares.append(n**2) # Without list comprehension
start = time.time()
squares = [n**2 for n in nums] # List comprehension
print(len(squares))
print(f"Time taken in seconds: {time.time() - start:.6f}")