import config
import telebot
from telebot import types
import database
import table
import timer
# понмиаю что пустые except нехорошо,
# к сожалению, писал в спешке
bot = telebot.TeleBot(config.Config.BOT_TOKEN)
base = database.Database()


def table_send(message, video):
    tb = table.Sheets()
    get = tb.read_material(video)
    msg_add = ''
    for ln in get[:10]:
        msg_add += ln[0]
        msg_add += '\n'

    if video:
        text = 'Посление видеоматериалы: \n'
    else:
        text = 'Последние дополнительные материалы: \n'

    bot.send_message(message.chat.id,
                     text=text
                     + msg_add)


def send_dop(message):
    tb = table.Sheets()
    get = tb.read_material(False)
    msg_add = ''
    for ln in get[:10]:
        msg_add += ln[0]
        msg_add += '\n'
    bot.send_message(message.chat.id,
                     text='Дополнительные мтаериалы: \n'
                          + msg_add)


def send_video(message):
    tb = table.Sheets()
    get = tb.read_material(True)
    msg_add = ''
    for ln in get[:10]:
        msg_add += ln[0]
        msg_add += '\n'
    bot.send_message(message.chat.id,
                     text='Посление видеоматериалы: \n'
                     + msg_add)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f'<b>Привет,'
        f' {message.from_user.first_name}!\n</b>, '
        + config.Config.START_msg,
        parse_mode='html')


@bot.message_handler(commands=['stop'])
def stoper(message):
    base = database.Database()
    try:
        base.del_user(message.chat.id)
    except:
        bot.send_message(
            message.chat.id, 'Вы не регестрировались')


@bot.message_handler()
def main_handler(message):
    base = database.Database()
    place = types.ReplyKeyboardMarkup()
    video = types.KeyboardButton('Видеоматериалы')
    dops = types.KeyboardButton('Дополнительные материалы')
    place.add(video, dops)
    if not (base.get_user_stat(message.chat.id)):
        try:
            period = int(message.text)
            base.write_user(message.chat.id, period)
        except ValueError:
            bot.send_message(
                message.chat.id,
                text='Неправильный интервал поробуй еще раз'
            )

        bot.send_message(
            message.chat.id,
            text='',
            reply_markup=place)

    else:
        try:
            cmnds = {'Дополнительные материалы': send_dop,
                     'Видеоматериалы': send_video,
                     'stop': stoper}

            cmnds[message.text](message)
        except:
            bot.send_message(
                message.chat.id,
                '',
                reply_markup=place)


# запускаем поток с напомниалкой вызовом обьекта
notificator = timer.Sendler(bot)
notificator()

bot.polling(none_stop=True, interval=0)

