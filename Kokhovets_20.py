# 5923848142:AAH6tPBfUhimDjFsBmqiWf-YThaHoNmhL9w
from sys import exit
import telebot
from telebot import types
token = '5923848142:AAH6tPBfUhimDjFsBmqiWf-YThaHoNmhL9w'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить!', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть!', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять!', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать!', callback_data='4')
    haha_btn = types.InlineKeyboardButton(text='Хочу шутку!', callback_data='5')
    stop_btn = types.InlineKeyboardButton(text='Завершить!', callback_data='6')
    keyboard.add(drink_btn, eat_btn, walk_btn, sleep_btn, haha_btn, stop_btn)
    return keyboard


@bot.message_handler(commands=['start', 'старт', 'поехали'])
def start_bot(mesage):
    klava = create_keyboard()
    bot.send_message(
        mesage.chat.id,
        'Добрый день!Выберите что хотите.',
        reply_markup=klava)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '1':
           bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://bulbul.ru/upload/iblock/142/voda.jpg',
                caption='Вода',
                reply_markup=create_keyboard()
            )
        if call.data == '2':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://avatars.mds.yandex.net/get-altay/2960979/2a0000017260a9d9f85eb44d3ab634dd7d7f/XXL',
                caption='Еда',
                reply_markup=create_keyboard()
            )
        if call.data == '3':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://static.tildacdn.com/tild6263-3836-4033-b430-306566623631/collar_04.jpg',
                caption='Прогулка',
                reply_markup=create_keyboard()
            )
        if call.data == '4':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStb_mH7ut5JPvS6zjhxeiL6jLbktmR_ZChDQ&usqp=CAU',
                caption='Сон',
                reply_markup=create_keyboard()
            )
        if call.data == '5':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://cs14.pikabu.ru/post_img/big/2022/08/10/5/1660112289183747485.jpg',
                caption='Шутка',
                reply_markup=create_keyboard()
            )
        if call.data == '6':
            bot.send_message(chat_id=call.message.chat.id, text='До скорой встречи!')
            exit(0)

bot.polling(non_stop=True)
