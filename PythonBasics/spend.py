print("Personal Spend money counter")
budget = int(input('Your budget: '))

categories = []  # список для названий расходов
expenses = []    # список для сумм расходов

while True:
    print("\nEnter expense data (or 'stop' to finish):")
    name = input("1. What did you spend money on? ")

    if name.lower() == 'stop':
        break

    amount = int(input("2. How much did you spend? "))

    categories.append(name)
    expenses.append(amount)
    print(f"Added: {name} - {amount} rub")

# Расчеты после выхода из цикла
total_spent = sum(expenses)
remaining = budget - total_spent

if expenses:  # если есть расходы
    max_expense = max(expenses)
    max_index = expenses.index(max_expense)
    max_category = categories[max_index]
else:
    max_expense = 0
    max_category = "No expenses"

# Вывод отчета
print("\n" + "="*40)
print("MONTHLY REPORT")
print("="*40)
print(f"Total budget: {budget} rub")
print(f"Total expenses: {total_spent} rub")
print(f"Remaining: {remaining} rub")
print(f"Largest expense: {max_category} ({max_expense} rub)")

if remaining >= 0:
    print("Status: Within budget ✅")
else:
    print("Status: Budget exceeded ❌")
