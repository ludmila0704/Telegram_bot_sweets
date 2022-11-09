import model
import handlers



def on_start_up(_):
    print('Сервер запущен')

model.bot.infinity_polling()
on_start_up()
