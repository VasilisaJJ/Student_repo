def change_line():
    line_index = int(input('Введите номер строки: ')) - 1
    data[line_index] = tuple(input('Введите изменения: ').split())

def get_line():
    s = list(input('Введите данные: ').split())
    return (int(s[0]), s[1], s[2], int(s[3]), int(s[4]), int(s[5]))

def insert(line):
    if line not in data:
        data.append(line)

def print_data(): # функция для красивого вывода БД в Питоне
    m=max([len(i) for i in titles])
    for i in titles:
        print(str(i).ljust(m+1, ' '), end='')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m+1, ' '), end='')
        print()

def write_to_file(filename): # получает имя файла .csv в проекте
    with open(filename, mode= 'w') as file: # открывает файл на режим записи write
        file.write(','.join(titles)+'\n')# объединение котежа-титульника в одну строку в БД в формате str
        for line in data:
            line = [str(i) for i in line] # перевод каждого элемента кортежа-строки в формат str
            file.write(','.join(line)+'\n') # объединение котежа-строки в одну строку в БД в формате str

def read_from_file(filename): # получает ТО ЖЕ имя файла .csv в проекте
    with open(filename, mode= 'r') as file: # открывает файл на режим записи read
        titles = tuple(file.readline().split(',')) # считывает строку титульников и переводит её в кортеж с помощью метода .split()
        data = [] # создание списка data для заполнения его строками информации
        for line in file:
            if line != '\n': # проверка на пустую строку
                line = line.split(',') # каждую строку в данных переводим в список
                data.append((int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5])))
    return titles, data

global data, titles

# columns, data = read_from_file('data.csv')
# print_data()
# insert(get_line())
# change_line()
# write_to_file('data.csv')

titles = ('id', 'name', 'lastname', 'age', 'height', 'weight') 
data = [                                                             # создание кортежа заголовков и списка данных в Программе
(1, 'Ivan', 'Ivanov', 14, 160, 50),
(2, 'Sasha', 'Sidorov', 15, 210, 40),
(3, 'Masha', 'Poradina', 30, 178, 70),
(4, 'Timur', 'Korolev', 44, 160, 120)
]

# write_to_file('New_data.csv') # запись информации в БД = перевод кортежей и 
# списка программы в формат str

titles, data = read_from_file('New_data.csv')
insert(get_line())
change_line()

write_to_file('New_data.csv')
print_data() # == print(columns, data) только красиво