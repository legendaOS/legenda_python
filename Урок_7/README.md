# Урок 7
# Цикл while

Цикл - конструкция позволяющая выполнять код несколько раз

Цикл while выполняется пока его условие истино

    i = 0
    while i < 10:
        print(i)
        i = i + 1

Программа выведт на экран числа от 0 до 9 включительно, т.к. проверяется что i < 10 

В условии цикла допустимо любое логическое выражение как и в if

    p = True
    while p:
        print('1')

Такой цикл никогда не завершится и программа будет бесконечно печатать цифру 1

например прерывание цикла можно организовать так

    cond = True
    i = 0
    while cond:
        print('ха-ха')
        i = i + 1
        if i == 10:
            cond = False

программа напечатает ха-ха 10 раз

## Принудительная остановка

Что бы завершить цикл можно воспользоваться командой break

    #программа w1
    i = 0
    while i < 100:
        i = i + 1
        print(i)
        if i == 13:
            break
            
Программа должна была вывести числа от 1 до 99, но на числе 13 она остановится

Аналогичную программу можно было бы написать и так

    #программа w2
    i = 0
    cond = True
    while i < 100 and cond:
        i = i + 1
        print(i)
        if i == 13:
            cond = False
            
 ## While / else
 
 Для цикла можно дописать else. Код в блоке else для цикла выполнится, если цикл не прерывали принудительно командой break
 
 Если исправить код для программ w1 и w2 следующим образом:
    
    #программа w1
    i = 0
    while i < 100:
        i = i + 1
        print(i)
        if i == 13:
            break
    else:
        print('ха-ха')
        
Эта программа на экран не выведет ха-ха

    #программа w2
    i = 0
    cond = True
    while i < 100 and cond:
        i = i + 1
        print(i)
        if i == 13:
            cond = False
    else:
        print('ха-ха')
        
А эта выведет!


## Continue

если в какой-то момент понадобится перескочить на следующий прогон цикла не выполняя какие то действия, то можно воспользоваться 
командой continue 

    i = 0
    while i < 1:
        i = i + 1
        print(1)
        print(2)
        if i == 1:
            continue
        print(3)
    
программа напечатает 1 и 2, и так как i == 1, то перепрыгнет на следующий прогон

        
    
    
    
