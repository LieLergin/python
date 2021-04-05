duration = int(input('Введите число: '))
minute = duration // 60
duration = duration - (minute * 60)

hour = minute // 60
duration = duration - (hour * 3600)

day = hour // 24
duration = duration - (day * 86400)

#month = duration // (30 * 24 * 3600)
#duration = duration - (month * 2592000)

print(day, 'день', hour, 'час', minute,'минут', duration, ' сек')