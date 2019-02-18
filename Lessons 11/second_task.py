"""Функция принимает две буквы и возвращает их в алфавитном порядку"""


def sravn(a, b):
    if a < b:
        return 'Bukva ' + a + ' sleduet pered bukvoy ' + b
    elif a > b:
        return 'Bukva ' + b + ' sleduet posle bukvi ' + a
    else:
        return 'Bukvi odinakovi ' + a


print(sravn('a', 'x'))
