import telebot
import work_data
from random import randint
from config import token

types = telebot.types
bot = telebot.TeleBot(token)
bost = .

#отработка /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, open('bot\stickers\hi.webp', 'rb'))
    keyboard=types.InlineKeyboardMarkup()
    start_work=types.InlineKeyboardButton(text='Работой 💼', callback_data='start_work')
    statistic=types.InlineKeyboardButton(text='Анализом 📊', callback_data='static')
    keyboard.add(start_work, statistic)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n - <b>{1.first_name}</b>, бот созданный чтобы помогать мне ввести учет доходов.".format(message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id,'Выбери, чем мы сейчас займемся',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'start_work': 
            #реакция при нажатии inline кнопки начать работать
            keyboard=types.InlineKeyboardMarkup()
            dosty=types.InlineKeyboardButton(text='🕊', callback_data='dosty')
            video=types.InlineKeyboardButton(text='🎞', callback_data='video')
            photo=types.InlineKeyboardButton(text='📸', callback_data='photo')
            other=types.InlineKeyboardButton(text='...', callback_data='other')
            back=types.InlineKeyboardButton(text='◀️', callback_data='back')
            keyboard.add(dosty, video, photo, other, back)
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='<b>ООО! Круто, дружище!\n</b>Хмм, а что именно будешь делать?', reply_markup=keyboard,parse_mode='html')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Начало работы')
        
        #отработка всех кнопок с типами работ с внесение в таблицу в зависимости от кнопки
        elif call.data == 'dosty' or call.data == 'video' or call.data == 'photo' or call.data == 'other': 
            big_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
            end = types.KeyboardButton('Закончить работу')
            big_keyboard.add(end)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='<b>Такс!</b>\nЯ записал, когда ты начал работать.\n<b><i>Удачной работы, брат!</i></b>',parse_mode='html',reply_markup=None)
            bot.send_message(call.message.chat.id, '_', reply_markup=big_keyboard)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Ах, жду когда закончится твоя смена')
            work_data.dates() 
            work_data.start()
            
            if call.data == 'dosty':    
                work_data.type('Доставка')
            elif call.data == 'video':
                work_data.type('Монтаж')
            elif call.data == 'photo':
                work_data.type('Фото ')
            elif call.data == 'other':
                work_data.type('Другое')
       
        elif call.data == 'back':
            keyboard=types.InlineKeyboardMarkup()
            start_work=types.InlineKeyboardButton(text='Работой 💼', callback_data='start_work')
            statistic=types.InlineKeyboardButton(text='Анализом 📊', callback_data='static')
            keyboard.add(start_work, statistic)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Выбери, чем мы сейчас займемся',reply_markup=keyboard)
        
        #отработка всех кнопок с кол-вом заказов
        elif call.data == 'one' or call.data == 'two' or call.data == 'three' or call.data == 'four' or call.data == 'five':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='<b>Записано</b>\nСколько заработал?',parse_mode='html')
            if call.data =='one':
                work_data.counts(1)
            elif call.data == 'two':
                work_data.counts(2)
            elif call.data == 'three':
                work_data.counts(3)
            elif call.data == 'four':
                work_data.counts(4)
            elif call.data == 'five':
                work_data.counts(5)

        elif call.data == 'static':
            excel = open('way_to_dream.xlsx','rb')
            bot.send_document(call.message.chat.id,excel)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Закончить работу':
            #выбираем рандомную гифку
            random = randint(1,3)
            if random == 1:
                vid = open('bot\stickers\sponge_bob_thumb_up_gif_compressed.gif','rb')
            elif random == 2:
                vid = open('bot\stickers\good_boy.webp', 'rb')
            elif random == 3:
                vid = open('bot\stickers\win.gif','rb')

            nums =  types.InlineKeyboardMarkup(row_width=8)
            one =   types.InlineKeyboardButton(text='1', callback_data='one')
            two =   types.InlineKeyboardButton(text='2', callback_data='two')
            three = types.InlineKeyboardButton(text='3', callback_data='three')
            four =  types.InlineKeyboardButton(text='4', callback_data='four')
            five =  types.InlineKeyboardButton(text='5', callback_data='five')
            nums.add(one,two,three,four,five)
            
            work_data.stop()

            bot.send_animation(chat_id=message.chat.id, animation=vid,reply_to_message_id=message.id)
            bot.send_message(chat_id=message.chat.id,text='<b>Ты легенда</b>\nЯ записал, время твоего начала\nВведи сколько заказов ты сделал',parse_mode='html',reply_markup=nums)
        else:
            #отработка всех сообщений формат x руб и внесение значение в таблицу
            if 'руб' in message.text:
                rubs = message.text  
                rubs = int(rubs.replace(' руб',''))
                vklad = round((int(rubs) * 0.55),1)
                mamy = round((int(rubs) * 0.15),1)
                work_data.money(rubs)

                link_bank = types.InlineKeyboardMarkup()  
                my_vklad = types.InlineKeyboardButton(text='Перевести на вклад', url='ya.ru') 
                mamy_bank =   types.InlineKeyboardButton(text='Перевод маме', url='t.me')
                link_bank.add(my_vklad,mamy_bank)
                #формируем вывод
                enter = bot.send_message(message.chat.id, f"<b>Вы заработали</b>: <code>{rubs}</code>\n<b>Нужно отложить:</b> <code>{vklad}</code>\n<b>Перевести маме:</b> <code>{mamy}</code>",parse_mode='html',reply_markup=link_bank)
                
                excel = open('way_to_dream.xlsx','rb')
                bot.send_document(message.chat.id,excel,reply_to_message_id=enter.id)
if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)
