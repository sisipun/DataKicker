import telebot
import math
import xgboost as xgb
from model.dev.xg_boost import xg_boost
from data.kicker_data import get_kicker_data, get_prediction_data, PLAYERS_COUNT

bot = telebot.TeleBot('264697554:AAFWzDTI9U6B-EtrZQZM-Eg5Ui9Nhth83cs')
x, y = get_kicker_data()
model = xg_boost(x, y)


@bot.message_handler(content_types=["text"])
def on_message(message):
    if not (__get_players(message)):
        return
    rp1, rp2, yp1, yp2 = __get_players(message)
    prediction = model.predict(xgb.DMatrix(get_prediction_data(rp1, rp2, yp1, yp2)))
    if math.fabs(round(prediction[0])) == 1:
        reply_message = 'Red team wins with prob: ' + str(prediction[0])
    else:
        reply_message = 'Yellow team wins with prob: ' + str(1 - prediction[0])
    bot.send_message(message.chat.id, reply_message)


def __get_players(message):
    prediction_players = message.text.split(',')
    if len(prediction_players) != 4:
        bot.send_message(message.chat.id, 'Sorry but data format is incorrect. It should be: "1, 2, 3, 4"')
        return None
    rp1, rp2, yp1, yp2 = prediction_players
    if not __is_number(rp1) or not __is_number(rp2) or not __is_number(yp1) or not __is_number(yp2):
        bot.send_message(message.chat.id, """Sorry but players id is incorrect. It should be: More than 0 and less or 
        equal to """ + str(PLAYERS_COUNT))
        return None
    return int(rp1), int(rp2), int(yp1), int(yp2)


def __is_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    return 1 <= number <= PLAYERS_COUNT


if __name__ == '__main__':
    bot.polling(none_stop=True)
