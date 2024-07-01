class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name


# Практическое задание № 1 - Атрибуты и методы объекта

dream_h = House('ЖК Дом мечты', 25)
elite_h = House('ЖК Элита', 10)

# dream_h.go_to(4)
# elite_h.go_to(44)

# Практическое задание № 2 - Специальные методы классов

print()
print(dream_h)
print(len(dream_h))
print(elite_h)
print(len(elite_h))
