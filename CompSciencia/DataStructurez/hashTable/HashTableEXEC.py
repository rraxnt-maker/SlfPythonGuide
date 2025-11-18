duty = {}

while True:
    print("\n=== My duty ===")
    print("1 - add duty")
    print("2 - complete duty")
    print("3 - Show all dictionary")
    print("4 - exit")

    i = int(input("\nChoose :  "))

    if i == 1:
        nameduty = input("Name: ")
        time = input("time of accomplishment: ")
        duty[nameduty] = time
        print(f"✅ Added: {nameduty} - {time}")  # Добавил подтверждение

    elif i == 2:
        d = input("which duty you finished? ")
        if d in duty:
            del duty[d]
            print(f"🎉 Completed: {d}")  # Добавил подтверждение
        else:
            print("There is no such duty")

    elif i == 3:
        if duty:
            print("duty list: ")
            for name, time in duty.items():  # ВСЕ строки с ОДИНАКОВЫМ отступом
                print(f"  {name} - {time}")
        else:
            print("Nothing! You can rest now")

    elif i == 4:
        print("Good luck")
        break

    else:
        print("cant understand u pls try again")
