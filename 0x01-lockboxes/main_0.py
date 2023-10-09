#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

# q = __import__('my-queue').MyQueue()
# print(q.display())
# print(q.is_empty())
# q.push(1)
# q.push(2)
# q.push(3)
# print(q.is_empty())
# print(q.display())
# print(q.pop())
# print(q.display())
# print(q.pop())
# print(q.pop())
# print(q.display())
