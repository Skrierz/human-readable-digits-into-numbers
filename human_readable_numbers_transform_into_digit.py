def func(input_, num=0):
    thous = 0
    mil = 0
    bil = 0
    zero = ['ноль']
    units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',
             'восемь', 'девять']
    units_ex = ['одна', 'две']
    eleven_to_nineteen = ['одиннадцать', 'двенадцать', 'тринадцать',
                          'четырнадцать', 'пятнадцать', 'шестнадцать',
                          'семнадцать', 'восемнадцать', 'девятнадцать']
    decimal = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
               'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousand = 'тысяч'
    million = 'миллион'
    billion = 'миллиард'

    # print(input_)
    for item in input_:
        if item in zero:
            return 0

        elif item in units:
            num += units.index(item) + 1

        elif item in units_ex:
            num += units_ex.index(item) + 1

        elif item in eleven_to_nineteen:
            num += eleven_to_nineteen.index(item) + 11

        elif item in decimal:
            num += (decimal.index(item) + 1) * 10

        elif item in hundreds:
            num += (hundreds.index(item) + 1) * 100

        elif thousand in item:
            thous = num * 1000
            num = 0

        elif million in item:
            mil = num * 1000000
            num = 0

        elif billion in item:
            bil = num * 1000000000
            num = 0
    num += thous + mil + bil
    return num


def main():
    input_ = input().split()

    a = func(input_)
    print(a)


if __name__ == '__main__':
    main()
