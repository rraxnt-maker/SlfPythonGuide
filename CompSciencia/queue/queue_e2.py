from collections import deque  # нужно импортировать deque

que = deque()  # используем deque вместо списка

def addcustomer():
    name = input("Enter customer name: ")
    que.append(name)
    print(f"Customer: {name} added")
    print(f"Queue size: {len(que)}")

def servecustomer():
    if len(que) == 0:
        print("Queue is empty")
        return None
    customer = que.popleft()  # popleft() для deque
    print(f"Customer {customer} served")
    return customer

def queueshow():
    if len(que) == 0:
        print("Queue is empty")
    else:
        print("Current queue:", list(que))

while True:
    print("\n=== Shop QUEUE ===")
    print("1 - Add customer")
    print("2 - Serve customer")
    print("3 - Show QUEUE")
    print("4 - Exit program")

    try:
        a = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if a == 1:
        addcustomer()  # нужно вызывать функцию со скобками!
    elif a == 2:
        servecustomer()  # нужно вызывать функцию со скобками!
    elif a == 3:
        queueshow()  # нужно вызывать функцию со скобками!
    elif a == 4:
        print("Goodbye!")
        break
    else:
        print("Wrong choice!")

