calls = 0  # создали переменную

def count_calls(call):
    global calls  #изменяем значение переменной
    calls += call
    return calls

def string_info(string):
    count_calls(1)     # строка в верхнем регистре, строку в нижнем регистре
    return (len(string),string.upper(),string.lower()) #ругается на скобки, хотя все норм

def is_contains(string_info, is_contains):
    string_info.lower()  # cоздаем две переменные
    new_is_contains = []   # возвращает True, если строка находится в этом списке
    count_calls(1)
    for i in is_contains:
        new_is_contains.append(i.lower())   # выводит False - если отсутствует
    return (string_info.lower() in new_is_contains)  #ругается на скобки, хотя все норм

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
