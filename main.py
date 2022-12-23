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



if __name__ == '__main__':
    task_2_2()
