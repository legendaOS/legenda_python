# Урок 9
### Словари

Словари - способ хранить много значений более организованно, чем в списках
Каждая запись в словаре представляет собой пару- ключ : значение

![Альтернативный текст](/Урок_9/d3a623b8ca09064f4d09c89167d89483.png)

Чтобы создать словарь нужно воспользоваться фигурными скобочками

    a = {'привет' : 'мир!', 2: 25, '2' : 23}

Чтобы получить какой-то эоемент словаря нужно обратиться к нему по имени

    print(a['привет']) # мир!
    print(a[2])  #25

Чтобы изменить значение в словаре нужно просто присвоить ему новое значение

    a['2'] = 5
    print(a['2']) #5

Так же можно и создать новую пару ключ:значение если их еще в словаре нет

    a[1] = 1
    print(a[1]) #1

В качестве ключа в словвре так же как и в качестве значения может быть все что угодно

Например можно создать словарь с ключами из списков а значениями из словарей

    a = {
        [1,2,3]: {
            1: 2,
            2: 3,
            'haha' : 'lol'
        },
        [2,3,4]: {
            1: 2,
            2: 3,
            'lol': 'kek'
        }
    }

### Методы словарей

dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.

### Перебор значений в словаре

    a = {.... какой-то словарь .....}
    i = 0
    keys = list(a.keys())
    while i < len(keys):
        print(f'{keys[i]} : {a[keys[i]]}')
        i += 1

Есть методы проще, но они будут на следующем уроке

[Магазин через словари с использованием цикла for](./magasin.py)