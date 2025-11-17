print("Hello There, this is your personal anket please enter future data")
name = str(input("Enter name: "))
age = int(input("Enter age: "))
marks = input("Enter three marks in , :")
markss = [int(x.strip()) for x in marks.split(",")]
awerage_mark = sum(markss) / len(markss)

print("=== Student Card ===")
print (f"Name : {name}")
print(f"Age : {age}")
print(f"Marks: {marks}")
print(f"Awerage Grade: {awerage_mark}")

if awerage_mark > 4.5 :
    print("Exellent Student")
elif awerage_mark > 3.5:
    print("Great Student")
elif awerage_mark > 2.5:
    print("Awerage student")
else:
    print("Bad Student")

