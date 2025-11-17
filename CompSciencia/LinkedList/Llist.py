class Friend:
    def __init__(self, friend):
        self.friend = friend
        self.next = None

friend1 = Friend("Semyon")
friend2 = Friend("Artyom")
friend1.next= friend2

def show_friends(firstFriend):
    current = firstFriend
    print("My friendz")
    while current is not None:
        print(f"- {current.friend}")
        current = current.next

show_friends(friend1)
