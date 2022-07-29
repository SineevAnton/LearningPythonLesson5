# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def gameStart():

    candyCount = 100
    maxTake = 28
    minTake = 1

    print(f'На столе лежит {candyCount} конфет.')

    while candyCount > 0:
        candyCount = playerMove(candyCount, minTake, maxTake)
        if candyCount == 0:
            print('Игрок победил!')
            break
        candyCount = computerMove(candyCount, minTake, maxTake)
        if candyCount == 0:
            print('Компьютер победил!')
            break

def playerMove(candyCount, minTake, maxTake):
    while True:

        if candyCount > maxTake:
            print(f'Вы можете взять от {minTake} до {maxTake} конфет.')
        else:
            print(f'Вы можете взять от {minTake} до {candyCount} конфет.')

        takenCount = int(input('Сколько конфет вы хотите взять? '))
        if minTake <= takenCount and takenCount <= maxTake and takenCount <= candyCount:
            break
        else:
            print('Неверный ввод, попробуйте еще раз.')

    candyCount -= takenCount
    print(f'Осталось {candyCount} конфет.')
    return candyCount

def computerMove(candyCount, minTake, maxTake):
    import random as rnd

    computerSpeech = ' конфет взял компьютер.'
    if candyCount <= maxTake:
        takenCount = candyCount
    elif candyCount % (maxTake + 1) != 0:
        takenCount = candyCount % (maxTake + 1)
    else:
        takenCount = rnd.randint(minTake, maxTake)
    print(str(takenCount) + computerSpeech)
    candyCount -= takenCount
    print(f'Осталось {candyCount} конфет.')
    return candyCount

gameStart()
