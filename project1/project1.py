﻿
from module1 import *

###1.Простейшие арифметические операции
###Написать функцию arithmetic, принимающую 3 аргумента: первые 2
###- числа, третий - операция, которая должна быть произведена над ними.
###Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; 
###/ — разделить (первое на второе). В остальных случаях вернуть строку 
###"Неизвестная операция".




answer=arithmetic(2.5, '+', 1.6)
print(answer)

while True:
    answer=arithmetic(input(),input(), input())
    print(answer)
    break

###2.Високосный год
###Написать функцию is_year_leap, принимающую 1 аргумент — год, и 
###возвращающую True, если год високосный, и False иначе.    

while True:

    if answer==is_year_leap(input('enter year:')):

        print('Leap year')
    else:
        print('ordinary year')
        break
    

###3.Квадрат
###Написать функцию square, принимающую 1 аргумент — сторону квадрата,
###и возвращающую 3 значения: периметр квадрата, площадь квадрата и 
###диагональ квадрата.

p=square(input('Rectangle:'))
s=square(input('Area:'))
d=square(input('Dioganal:'))

print(f'Rectangle:{p}')
print(f'area:{s}')
print(f'diagonal:{d}')


###4.Времена года
###Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
###которому этот месяц принадлежит (talv, kevad, suvi или sügis).





while True:
    print(season(int(input('enter month:'))))
            
    

##5.Банковский вклад
##Пользователь делает вклад в размере a евро сроком на years лет под 10% 
##годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги 
## прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

p=int(float(input("how a lot of money? ")))

years=int(float(input("how many years  for ? ")))

print(bank(p,years))

##6.Простые числа
##Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, 
##и возвращающую True, если оно простое, и False - иначе.

ordinary=int(input('enter a num:'))
print(is_prime(ordinary))


##7.Правильная дата
##Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
##Вернуть True, если такая дата есть в нашем календаре, и False иначе.

d=int(input("enter day"))
m=int(input("enter month"))
y=int(input("enter year"))

print(date(y,m,d))



##8.XOR-шифрование
##Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую 
##нужно зашифровать, и ключ шифрования, которая возвращает строку,
##зашифрованную путем применения функции XOR (^) над символами строки
##с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной 
##строке и ключу восстанавливает исходную строку.

strg=input('crypt:')
key=46
print('original:\t', strg )
encr_strg=xor_cipher(strg, key) 
print('encript:\t',encr_strg)
encr_strg=input('decryp:')
print('encript:\t',xor_cipher(encr_strg,key))


    

