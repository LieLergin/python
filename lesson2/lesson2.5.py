goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
print(f'{rub} руб {kk:02.0f} коп')