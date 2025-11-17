"""
Queue is a linear collection of items where items are inserted and removed in a particular order. The queue is also called a FIFO Data Structure because it follows the "First In, First Out" principle i.e., the item that is inserted in the first is the one that is taken out first.
"""
queue = []


queue.append("Danial")
queue.append("Artem")
queue.append("Semyon")

print (queue)

first = queue.pop(0)
print(f"serving {first}")
print(queue)
