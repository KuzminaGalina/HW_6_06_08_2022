# 1- Определить, присутствует ли в заданном списке строк, некоторое число

def find_number(element, number):
    # string = ' '.join(element)
    # return str(number) in string
    return list(filter(lambda result: str(number) in result, element))


print(find_number(['Ма0ма', 'сши0ла', 'мн1е', 'штаны', '893' ], 0))

