class FamilyM:
    def __init__(self, name):
        self.name = name
        self.kid = []

grandpa = FamilyM("Ivan")
granny = FamilyM("Lida")
father = FamilyM("Semen")
mother = FamilyM("Alice")
son = FamilyM("Danial")
daugter = FamilyM("Artyom")


grandpa.kid.append(father)
granny.kid.append(father)
father.kid.extend([son, daugter])

def show_family(parent, level=0):
    indent = "  " * level
    print(indent + parent.name)
    for child in parent.kid:
        show_family(child, level + 1)

# Показываем древо
print("Семья Ивана:")
show_family(grandpa)

print("\nСемья Лиды:")
show_family(granny)
