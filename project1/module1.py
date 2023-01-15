from math import isqrt


def arithmetic(a1:float,symbol:str, a2:float)-> any:
    """calculator
    + plus, - minus, * multiple, / devide
    : param float a1: the first digit
    : param float a2: second digit
    : param str symbol: action
    : rtype: var undefined type

    """
    if symbol in ['+','-','/','*']:
        
        if symbol=='/' and a2==0:
            answer='Div/0'
        else:
            answer=eval(str(a1)+symbol+str(a2))

    else:
        answer='Unknow action !'

    return answer



###eval - as long as it is arethmetic action does it

### any - does any type of action

### bool -

###2Високосный год
###Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(leap_year:int):
    """ return True if year leap year, as long as the oposite False
    :param int year: Year number
    :rtype: bool Function answer certain formadis
    """
    leap_year=int(leap_year)

    if leap_year%4==0:

        answer1=True
    else:

        answer1=False

    return answer1


###3Квадрат
###Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.



def square(a: float):
    """
    """
    try:
        a=float(a)
        if a>0:

            p=4*a
            s=a*a
            d=a*isqrt(2)
            return p,s,d
        else:
            v='---'
            return v
    except:
        v='---'
        return v



###4Времена года
###Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
###которому этот месяц принадлежит (talv, kevad, suvi или sügis).


def season(month):
    if month in (1,2,12):
        return 'winter'
    elif month in (3,4,5):
        return 'spring'
    elif month in(6,7,8):
        return 'summer'
    elif month in(9,10,11):
        return 'autumn'
    else:
        return 'Error'




##5.Банковский вклад
##Пользователь делает вклад в размере a евро сроком на years лет под 10% 
##годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги 
## прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

def bank(p,years):
    """ p= money, it can take 2 position
    :param p:int or float
    :param years: int or float
    """
    for each_year in range(years):
        p = (p * 1.1)
    return p


##6.Простые числа
##Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, 
##и возвращающую True, если оно простое, и False - иначе.

def is_prime(ordinary):
    #"""ordinary num divides without residue and only by itself
    #:param ordinary: int
    #"""
    for i in range(2, (ordinary//2)+1):
        if ordinary % i == 0:
            return False
    return True 

##7.Правильная дата
##Написать функцию date, принимающую 3 аргумента — день, месяц и год.
##Вернуть True, если такая дата есть в нашем календаре, и False иначе.

import datetime
def date(y:int,m:int,d:int):
    """based on datetime
    :param y:int
    :param m:int
    :param d:int
    """
    try:
        data=datetime.date(y,m,d)
        print(data)
        print("existing date")
    except:
        print("such date doesnt exist")

        return date
 

##8.XOR-шифрование
##Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую
##нужно зашифровать, и ключ шифрования, которая возвращает строку, 
##зашифрованную путем применения функции XOR (^) над символами строки с 
##ключом. Написать также функцию XOR_uncipher, которая по зашифрованной 
##строке и ключу восстанавливает исходную строку.

def xor_cipher(str,key):
    """encrypts the string 
    with key.
    """
    encript_str=""
    for letter in str:
        encript_str+=chr(ord(letter)^key)

    return encript_str




    

    

    

    

   

        


  
