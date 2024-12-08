print('简易扑克牌游戏')
import random

#生成一幅扑克牌
listcards = []
for i in range(1,55):
    listcards.append(i)
print('初始化：', listcards)

#进行洗牌
random.shuffle(listcards)
print('洗牌后：', listcards)

#进行切牌
a = random.choice(listcards)
print('切牌：%d' % a)

listcut = listcards[a:] + listcards[:a]
print('切牌后：', listcut)

#为玩家分发手牌
deck1 = []
deck2 = []
deck3 = []          #初始化三手牌
for i in range(17):
    deck1.append(listcut.pop())
    deck2.append(listcut.pop())
    deck3.append(listcut.pop())
print('玩家一：', deck1)
print('玩家二：', deck2)
print('玩家三：', deck3)
print('剩余的三张牌', listcut)

#对玩家手牌排序（理牌）
deck1.sort(reverse=True)
deck2.sort(reverse=True)
deck3.sort(reverse=True)
print('玩家一：', deck1)
print('玩家二：', deck2)
print('玩家三：', deck3)

#随机选出地主玩家
listplayer = ['玩家一', '玩家二', '玩家三']
b = random.choice(listplayer)  #随机取数
print('地主为：',  b)

#为地主玩家分发底牌
if b == '玩家一':
    deck1 = deck1[:]+listcut[:]
    deck1.sort(reverse=True)
    deck2.sort(reverse=True)
    deck3.sort(reverse=True)
    print('地主玩家一：', deck1)
    print('玩  家  二：', deck2)
    print('玩  家  三：', deck3)
elif b == '玩家二':
    deck2 = deck2[:]+listcut[:]
    deck1.sort(reverse=True)
    deck2.sort(reverse=True)
    deck3.sort(reverse=True)
    print('玩  家  一：', deck1)
    print('地主玩家二：', deck2)
    print('玩  家  三：', deck3)
else:
    deck3 = deck3[:]+listcut[:]
    deck1.sort(reverse=True)
    deck2.sort(reverse=True)
    deck3.sort(reverse=True)
    print('玩  家  一：', deck1)
    print('玩  家  二：', deck2)
    print('地主玩家三：', deck3)
