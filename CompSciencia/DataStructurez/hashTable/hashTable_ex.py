duty = {}

while True:
    print("\n=== My duty ===")
    print("1 - add duty")
    print("2 - complete duty")
    print("3 - Show all dictionary")
    print("4 - exit")

    i = int(input("\nChooze :  "))

    if i == 1:
        nameduty = input("Name: ")
        time = input("time of accomplishment: ")
        duty[nameduty]= time
    elif i == 2:
        d = input("which duty you finished?")
        if d in duty:
            del duty[d]
        else:
            print("There is no such duty")
    elif i == 3:
        if duty:
            print("duty list: ")
                for name, time in duty.items():
                print(f"  {name} - {time}")

        else:
            print("Nothing You can rest now")
    elif i == 4:
        print("Good luck")
        break
    else:
        print("cant understand u pls try again")
