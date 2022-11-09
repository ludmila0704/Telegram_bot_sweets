
# from cgitb import text
# from imaplib import Commands
import model,controller
import view
from telebot import types


@model.bot.message_handler(commands=['start','help'])
def command_start(message):
	#view.get_button()
	kb=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)#,one_time_keyboard=False)
	btn1=types.KeyboardButton(text= model.rules)
	btn2=types.KeyboardButton(text=model.game)
	kb.add(btn1,btn2) 
	
	model.bot.send_message(message.chat.id,f'{message.from_user.first_name}, {view.game()}',reply_markup=kb)
	model.player1_name = message.from_user.first_name
	


@model.bot.message_handler(func=lambda message: message.text=='Правила игры')
def command_rules(message):
	message.text=view.view_rules_game()
	model.bot.send_message(message.chat.id,f'{message.text}')

@model.bot.message_handler(func=lambda message: message.text=='Поиграем в конфетки')
def game(message):
	model.bot.send_message(message.chat.id,f'{message.from_user.first_name}, {view.lets_go()}')
	whosStep=controller.random_step()
	if whosStep==0:
		model.bot.send_message(message.chat.id,f'{message.from_user.first_name}, {model.ans_first}')
		model.bot.send_message(message.chat.id,model.ans_your_step)
		
		
	else:
		model.bot.send_message(message.chat.id,f'{model.ans_bot_first} {model.player2_name}')
		step=controller.bot_step(1)
		model.bot.send_message(message.chat.id,f'{step} {model.ans_bot_step}. {model.ans_sweet_on_table} {model.sweetsOnTable}.')
		model.bot.send_message(message.chat.id,model.ans_your_step)

	
@model.bot.message_handler(func=lambda message: message.text.isdigit())
def continew_game(message):
	step=int(message.text)
	if model.sweetsOnTable>0:# controller.is_valid_sweet(step):
		#controller.play_user(step)
		if  controller.is_valid_sweet(step):#model.sweetsOnTable>0:
			controller.play_user(step)
			model.bot.send_message(message.chat.id,f'{model.ans_step} {step}. {model.ans_sweet_on_table} {model.sweetsOnTable}.')
			#step=controller.bot_step(2)
			if model.sweetsOnTable>0:
					step=controller.bot_step(2)
					if model.sweetsOnTable>0:
						model.bot.send_message(message.chat.id,f'{step} {model.ans_bot_step}. {model.ans_sweet_on_table} {model.sweetsOnTable}. {model.ans_your_step} {message.from_user.first_name}? ')
					else:
						model.sweetsOnTable=0
						model.bot.send_message(message.chat.id,f'{model.ans_bot_win} {model.player2_name}')
			else:
				model.bot.send_message(message.chat.id,f'{message.from_user.first_name}{model.ans_win_player}')
		else:
			message_error=view.error_input()
			model.bot.send_message(message.chat.id,message_error)
			#model.bot.send_message(message.chat.id,f'{message.from_user.first_name}{model.ans_win_player}')
			 #model.bot.send_message(message.chat.id,view.game_false)
	else:
		#message_error=view.game_false()
		model.bot.send_message(message.chat.id,view.game_false())
		# message_error=view.error_input()
		# model.bot.send_message(message.chat.id,message_error)
