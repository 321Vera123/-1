print("Загадайте животное, а я попробую угадать")
print("Отвечайте только да или нет")

if input('это животное большое?') == ' да':
    if input("У него есть полоски?") == " да":
        if input("Оно оранжевого цвета?") == " да":
            print("Я думаю это тигр")
        else:
            print("Может быть это зебра?")
    else:
        if input("Оно живет в Африке?") == " да":
            print("Я думаю это слон")
        else:
            print("Может быть это медведь?")
else:
    if input("Оно бывает разных цветов?") == " да":
        print("Я думаю это кошка")
    else:
        print("Я думаю это мышь")

if input('Получилось отгадать?') == " да":
    print("Ура!")
else:
    print("Не вышло, попробуй загадать другое животное")
