from collections import deque

# Create a queue
queue = deque()

# Enqueue 4 values
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print("After enqueuing 4 values:")
print(f"Queue: {list(queue)}")

# Dequeue 1 value
dequeued_value = queue.popleft()
print(f"\nDequeued value: {dequeued_value}")

# Display final queue
print(f"Queue after dequeue: {list(queue)}")
