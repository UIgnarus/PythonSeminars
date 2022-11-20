# lambda функции

#sum = lambda x: x + 10
def lambda_f():
    def select(f, col):
        return [f(x) for x in col]
    def where(f, col):
        return [x for x in col if f(x)]
    data = '1 2 3 5 8 15 23 38'.split()
    data = select(int, data)
    data = where(lambda e: not e % 2, data)
    data = list(select(lambda e: (e, e**2), data))
    print(data)
# lambda_f()

def lambda_f2():
    data = '1 2 3 5 8 15 23 38'.split()
    data = list(map(int, data))
    data = list(filter(lambda e: not e % 2, data))
    data = list(map(lambda e: (e, e**2), data))
    print(data)
#lambda_f2()

# Функция map (f, объект)
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

# Функция filter (f, объект)
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
#print(list(zip([1, 2, 3], [ 'о', 'д', 'т'], ['f','s','t'])))

# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]
