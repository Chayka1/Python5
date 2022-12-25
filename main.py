def task_1_1():
    choise = 'д'

    if choise.upper() == 'Д':
        print('Вы ввели д!')


def task_1_2():
    mystring = 'Привет я Максим'

    total = 0

    for st in mystring:
        if st.isspace():
            total += 1

    print(total)


def task_1_3():
    mystring = 'Я родился в 2004 году'

    total = 0

    for st in mystring:
        if st.isdigit():
            total += 1

    print(total)


def task_1_4():
    mystring = 'Привет'

    total = 0

    for st in mystring:
        if st.islower():
            total += 1

    print(total)


def task_1_5():
    mystring = 'main.com'

    if mystring.endswith('.com'):
        print('True')
    else:
        print('False')


def task_1_6():
    mystring = 'тимур'

    mystring = mystring.replace('т', 'Т')

    print(mystring)


def task_1_7():
    mystr = '12345'[::-1]

    print(mystr)


def task_1_8():
    mystring = 'Максим'

    my = mystring[:3]

    print(my)


def task_1_9():
    mystring = 'Максим'

    my = mystring[-3:]

    print(my)


def task_1_10():
    mystring = 'пирожки>молоко>стряпня>яблочный пирог>мороженое'

    my = mystring.split('>')

    print(my)


def task_2_1():
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')

    short_name = name[:1]
    short_last_name = last_name[:1]
    short_patronymic = patronymic[:1]

    print(f'{short_name}.{short_last_name}.{short_patronymic}')


def task_2_2():
    numbers = input('Введите числа: ')

    nums = list(numbers)

    total = 0
    for mynums in nums:
        total += int(mynums)

    print(total)


def task_2_3():
    date = input('Введите дату (дд/мм/гггг): ')

    altered_date = date.split('/')

    months = ['января', 'февраля', 'марта', 'апреля', 'майя', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    i = int(altered_date[1])
    month = months[i-1]

    print(f'{altered_date[0]} {month} {altered_date[2]} г.')


def task_2_4():
    number_of_phone = input('Введите номер телефона: ')

    a = []
    b = []

    numbers = number_of_phone.split('-')

    i = list(numbers[1])
    j = list(numbers[2])

    for nums in i:
        if nums == 'A' or nums == 'B' or nums == 'C':
            num = 2
            a.append(num)
        elif nums == 'D' or nums == 'E' or nums == 'F':
            num = 3
            a.append(num)
        elif nums == 'G' or nums == 'H' or nums == 'I':
            num = 4
            a.append(num)
        elif nums == 'J' or nums == 'K' or nums == 'L':
            num = 5
            a.append(num)
        elif nums == 'M' or nums == 'N' or nums == 'O':
            num = 6
            a.append(num)
        elif nums == 'P' or nums == 'Q' or nums == 'R' or nums == 'S':
            num = 7
            a.append(num)
        elif nums == 'T' or nums == 'U' or nums == 'W':
            num = 8
            a.append(num)
        elif nums == 'W' or nums == 'X' or nums == 'Y' or nums == 'Z':
            num = 9
            a.append(num)

    for nums in j:
        if nums == 'A' or nums == 'B' or nums == 'C':
            num = 2
            b.append(num)
        elif nums == 'D' or nums == 'E' or nums == 'F':
            num = 3
            b.append(num)
        elif nums == 'G' or nums == 'H' or nums == 'I':
            num = 4
            b.append(num)
        elif nums == 'J' or nums == 'K' or nums == 'L':
            num = 5
            b.append(num)
        elif nums == 'M' or nums == 'N' or nums == 'O':
            num = 6
            b.append(num)
        elif nums == 'P' or nums == 'Q' or nums == 'R' or nums == 'S':
            num = 7
            b.append(num)
        elif nums == 'T' or nums == 'U' or nums == 'W':
            num = 8
            b.append(num)
        elif nums == 'W' or nums == 'X' or nums == 'Y' or nums == 'Z':
            num = 9
            b.append(num)






if __name__ == '__main__':
    task_2_4()
