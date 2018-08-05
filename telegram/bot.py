import telebot
from model.dev.log_regression import fit
from data.kicker_data import get_kicker_data, get_prediction_data

bot = telebot.TeleBot('264697554:AAFWzDTI9U6B-EtrZQZM-Eg5Ui9Nhth83cs')
x, y = get_kicker_data()
lr = fit(x, y)


@bot.message_handler(content_types=["text"])
def on_message(message):
    prediction_players = message.text.split(',')
    if len(prediction_players) != 4:
        bot.send_message(message.chat.id, 'Sorry but data format is incorrect. It should be: "1, 2, 3, 4"')
        return
    rp1, rp2, yp1, yp2 = prediction_players
    prediction = lr.predict(get_prediction_data(rp1, rp2, yp1, yp2))
    if prediction[0] == 1:
        reply_message = 'Red team wins'
    else:
        reply_message = 'Yellow team wins'
    bot.send_message(message.chat.id, reply_message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
