first_name = 'Петя'
first_speed = float(input())
second_name = 'Вася'
second_speed = float(input())
third_name = 'Толя'
third_speed = float(input())

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name

if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name

print(f"1. {first_name}")
print(f"2. {second_name}")
print(f"3. {third_name}")
