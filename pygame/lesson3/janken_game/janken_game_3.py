import random
 hands = ['グー', 'チョキ', 'パー']
you_win = 0
com_win = 0
print('じゃんけんスタート')

for i in range(5):
    print('じゃんけん')
    print('0:グー 1:チョキ 2:パー')
    you = int(input('あなたの手を入力してください:'))
    com = random.randint(0, 2)
    print('コンピュータの手:', hands[com])

    if you == com:
        print('あいこ')
    elif (you == 0 and com == 1) or (you == 1 and com == 2) or (you == 2 and com == 0):
        print('あなたの勝ち')
        you_win += 1
    else:
        print('コンピュータの勝ち')
        com_win += 1

print('あなたの勝ち:', you_win, '回')
print('コンピュータの勝ち:', com_win, '回')
if you_win > com_win:
    print('あなたの勝ちです')
elif you_win < com_win:
    print('コンピュータの勝ちです')
else:
    print('引き分けです')
print('じゃんけん終了')