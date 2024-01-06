# Здесь мы инициализируем пустое игровое поле размером 3х3 (общее количество ячеек - 9)
igrovoe_pole = [' ' for _ in range(9)]

# Функция для отображения игрового поля на экране. Каждая строка игрового поля формируется в отдельной переменной
def pechat_igrovogo_polya():
    stroka1 = "|{}|{}|{}|".format(igrovoe_pole[0], igrovoe_pole[1], igrovoe_pole[2])
    stroka2 = "|{}|{}|{}|".format(igrovoe_pole[3], igrovoe_pole[4], igrovoe_pole[5])
    stroka3 = "|{}|{}|{}|".format(igrovoe_pole[6], igrovoe_pole[7], igrovoe_pole[8])
    print(stroka1)
    print(stroka2)
    print(stroka3)

# Функция для выполнения хода игроком

def hod_igroka(icon):

    print("Ход делает игрок " + ('1' if icon == 'X' else '2'))

    while True:

        try:

            vybor = int(input("Введите свой ход (от 1 до 9): "))

            if vybor in range(1, 10):

                if igrovoe_pole[vybor - 1] == ' ':

                    igrovoe_pole[vybor - 1] = icon

                    break

                else:

                    print("Это место уже занято!")

            else:

                print("Ваш ввод должен быть в пределах от 1 до 9")

        except ValueError:

            print("Пожалуйста, введите число.")

# Функция для проверки условий выигрыша игрока. Проверка происходит по горизонталям, вертикалям и диагоналям
def proverka_na_pobedu(icon):
    if (igrovoe_pole[0] == icon and igrovoe_pole[1] == icon and igrovoe_pole[2] == icon) or \
       (igrovoe_pole[3] == icon and igrovoe_pole[4] == icon and igrovoe_pole[5] == icon) or \
       (igrovoe_pole[6] == icon and igrovoe_pole[7] == icon and igrovoe_pole[8] == icon) or \
       (igrovoe_pole[0] == icon and igrovoe_pole[3] == icon and igrovoe_pole[6] == icon) or \
       (igrovoe_pole[1] == icon and igrovoe_pole[4] == icon and igrovoe_pole[7] == icon) or \
       (igrovoe_pole[2] == icon and igrovoe_pole[5] == icon and igrovoe_pole[8] == icon) or \
       (igrovoe_pole[0] == icon and igrovoe_pole[4] == icon and igrovoe_pole[8] == icon) or \
       (igrovoe_pole[2] == icon and igrovoe_pole[4] == icon and igrovoe_pole[6] == icon):
        return True
    else:
        return False


# Начало игры, объяснение правил.

print("                             ДОБРЫЙ ДЕНЬ!")
print("Сейчас мы сыграем в одну из самых популярных игр в крестики-нолиики!")
print()
print("Правила просты: игроки по очереди ставят свои знаки (X или O) на пустые клетки игрового поля.") 
print("Выигрывает тот, кто первым выстроит в ряд 3 своих знака по вертикали, горизонтали или диагонали.")
print()
print("Ход вводится как число от 1 до 9, что соответствует следующим позициям клеток на поле:")
print()
print("1 - верхний левый угол,     2 - верхний центр, 3 - верхний правый угол,")
print()
print("4 - средний левый,          5 - центр,         6 - средний правый,")
print()
print("7 - нижний левый угол,      8 - нижний центр,  9 - нижний правый угол.")
print()
print()
print()
print("Поехали!")
print()
print()
print()

# Основной игровой цикл, который выполняется до тех пор, пока не произойдет выигрыш или не закончатся свободные ячейки
icon = 'X'
while True:
  
  hod_igroka(icon)
  pechat_igrovogo_polya()
  if proverka_na_pobedu(icon):
      print(icon + " выиграли! Поздравляем!")
      break
  elif not ' ' in igrovoe_pole:
      print("Ничья!")
      break

  icon = 'O' if icon == 'X' else 'X'
  
