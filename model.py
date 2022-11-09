import telebot

bot = telebot.TeleBot("---------")
message=''
sweetsOnTable=150

maxCountSweet = 28
#stepSweet = 0
sweetPlayer=0
player1_name = ''
player2_name = 'Clever Bot'
# message_rules='Игра с конфетами\nПравила: На столе лежит 150 конфет.\n'\
# 'Играют два игрока: бот и вы, делая ход друг после друга.\n'\
# 'Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.\n\n'\
# 'Все конфеты оппонента достаются сделавшему последний ход.\n'\

rules ='Правила игры'
game='Поиграем в конфетки'
# ответы 
ans_your_step = 'Твой ход. Cколько конфет ты возьмешь, '
ans_step='Вы взяли '
ans_sweet_on_table = 'На столе осталось'
ans_bot_first = 'Итак, первый ходит'
ans_first =' Вы ходите первым (ой)!'
ans_bot_step='конфет(ы) забрал бот '
ans_bot_win='Бот забрал все конфетки. Выиграл '
ans_win_player=', вы выиграли. Поздравляем!!!'



