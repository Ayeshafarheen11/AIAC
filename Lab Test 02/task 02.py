def avg(scores):
    return sum(scores) / len(scores)

try:
    print(avg([]))
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
