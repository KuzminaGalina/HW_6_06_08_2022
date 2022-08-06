# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def second_in_lst(user_lst:list):
    second_match = []
    count= 0
    history = []
    for x in user_lst:
        count = 0
        for i in range(0,len(user_lst)):
            if x in user_lst[i] and not x in history:
                count += 1
                if count == 2:
                    history.append(x)
                    second_match.append((i, user_lst[i]))
    return second_match

user_lst = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe", "asd", "bbb"]
print(second_in_lst(user_lst))