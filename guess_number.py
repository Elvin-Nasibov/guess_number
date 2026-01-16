# print('halo')
import random

num = random.randrange(101)
print("Добро пожаловать в числовую угадайку")
print("Я загадал число в диапазоне от 0 до 100")
print("Попробуй-ка отгадать это число!")


def is_digit(n):
    if n.isdigit():
        if int(n) in range(101):
            return rand_number(n)
        else:
            print("Дурачок, чтоли??")
            print("Это число не в указанном диапазоне!")
            print("!!!ДИАПАЗОН ОТ 0 ДО 100!!!")
            return is_digit(input())
    else:
        print("Дурачок, чтоли??")
        print("Нужно писать целое ЧИСЛО в указанном диапазоне!!!")
        return is_digit(input())


def rand_number(n):
    n = int(n)
    while n != num:
        if n > num:
            print("Слишком много, попробуйте еще раз")
            return is_digit(input())
        elif n < num:
            print("Слишком мало, попробуйте еще раз")
            return is_digit(input())
    else:
        return "Вы угадали, поздравляем!"
        


print(is_digit(input()))
print('Спасибо за игру. Еще увидимся...')


# print('sss')
