import random
def kolona_1():
    shifr = [i for i in range(3, 21)]
    win = random.choice(shifr)
    return win
win = int(kolona_1())
print(win)
parol_1 =int (input('введите число:' ))
print(parol_1)
parol_2 = int (input('второе число: ' ))
print(parol_2)
win_1 = parol_1 + parol_2
if 0 == win % win_1 :
    print('Верный пароль')
else:
    print('Вы не разгадали пароль')
def find_password(win):
    result = []
    for a in range(1, win):
        for j in range(a + 1, win):
            if 0 == win % ((a + j)):
                pas_n = str(a) + str(j)
                result.append(pas_n)
        return result
vse_paroli = find_password(win)
print(vse_paroli)










