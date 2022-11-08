
def Animal_year(x):
    animal_of_the_year = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна",
                          "Петух", "Собака", "Свинья", "Крыса", "Бык",
                          "Тигр", "Заяц"]
    return str(animal_of_the_year[(x+4) % 12])

print("2000 - " + Animal_year(2000))
print("2001 - " + Animal_year(2001))
print("2023 - " + Animal_year(2023))
print("1998 - " + Animal_year(1998))
print("1973 - " + Animal_year(1973))
