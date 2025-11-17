
que = []

while True:
    i = int(input("Enter: 1 to join queue, 2 to slide , 3 show queue, 4 exit program: "))
    if i == 1:
        name = input("Enter Ur name ")
        que.append(name)
        print(f"{name} joined queue")
    elif i == 2:
        if que:
            first = que[0]
            print(f"{first} slided")
            que.pop(0)
        else:
            print("Queue is empty! No one to slide.")
    elif i == 3:
        print(que)
    elif i == 4:
        break
    else:
        print("wrong option PLS try again")

