running = True

while running:
    print('Мы ещё в цикле')
    number = int(input('Введите ваш возраст: '))
    if number > 5:
        print('Выходим из цикла')
        break

print('Завершение программы')
