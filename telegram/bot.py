import math
import telebot
import xgboost as xgb
from data.kicker_data import get_prediction_data
from model.dev.xg_boost import xg_boost
from telegram.config import token
from util.constant import PLAYERS_COUNT
from util.message_validator import is_number

bot = telebot.TeleBot(token)
model = xg_boost()


@bot.message_handler(content_types=["text"])
def on_message(message):
    if not (__get_players(message)): return
    rp1, rp2, yp1, yp2 = __get_players(message)
    prediction = model.predict(xgb.DMatrix(get_prediction_data(rp1, rp2, yp1, yp2)))
    if math.fabs(round(prediction[0])) == 1:
        reply_message = 'Red team wins with prob: ' + str(round(prediction[0] * 100, 1)) + '%'
    else:
        reply_message = 'Yellow team wins with prob: ' + str(round((1 - prediction[0]) * 100, 1)) + '%'
    bot.send_message(message.chat.id, reply_message)


def __get_players(message):
    prediction_players = message.text.split(',')
    if len(prediction_players) != 4:
        bot.send_message(message.chat.id, 'Sorry but data format is incorrect. It should be: "1, 2, 3, 4"')
        return
    rp1, rp2, yp1, yp2 = prediction_players
    if not is_number(rp1) or not is_number(rp2) or not is_number(yp1) or not is_number(yp2):
        bot.send_message(message.chat.id,
                         'Sorry but players id is incorrect. It should be: More or equal to 1 and less or equal to ' +
                         str(PLAYERS_COUNT))
        return
    return int(rp1), int(rp2), int(yp1), int(yp2)


if __name__ == '__main__':
    bot.polling(none_stop=True)
