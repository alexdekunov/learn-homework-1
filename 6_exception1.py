"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():

    while True:
        ask = input("Как дела? ... ")
        if ask == 'Хорошо' or ask == 'хорошо':
            print('Отлично')
            break
        else:
            print('Попробуй ещё раз')

if __name__ == "__main__":
    hello_user()
