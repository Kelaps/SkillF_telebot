import telebot
from configs import TOKEN
from configs import keys
from extension2 import ConverterExeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Приветствие!'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    text += '\n'.join(f'{i+1}) {key}' for i, key in enumerate(keys.keys()))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])    
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    quote, base, amount = values

    if len(values) != 3:
         raise ConverterExeption("Неверное количество параметров")
        
    total_base = CryptoConverter.convert(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {int(total_base)}'
    bot.send_message(message.chat.id, text)





bot.polling()


