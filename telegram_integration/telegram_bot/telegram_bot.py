import telebot
import requests
import telegram_urls
import telegram_markup
import telegram_settings
import telegram_func
import json

bot = telebot.TeleBot(telegram_settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    text = message.text

    data = {
        'chat_id': chat_id,
        'text': text
    }
    print(chat_id)
    response = requests.post(telegram_urls.verify_url, data)

    if response.status_code == 200:

        response_text = response.json().get('response')
        username = str(response.json().get('username'))
        print(response_text,response_text)
        if response_text == 'registerd':
            bot.send_message(chat_id, f"Hii " + username,
                             reply_markup=telegram_markup.logout_markup)
        else:
            bot.reply_to(message, "Hi, I can't identify you please login or register",
                         reply_markup=telegram_markup.not_logined_markup)

    else:
        print('Verification failed', response)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    data = {
        'chat_id': chat_id,
        'text': text
    }
    print(chat_id)
    response = requests.post(telegram_urls.verify_url, data)

    if response.status_code == 200:

        response_text = response.json().get('response')
        username = str(response.json().get('username'))

        if response_text == 'registerd':
            bot.send_message(chat_id, f"Hii " + username,
                             reply_markup=telegram_markup.logout_markup)
        else:
            bot.reply_to(message, "Hi, I can't identify you please login or register",
                         reply_markup=telegram_markup.not_logined_markup)

    else:
        print('Verification failed', response)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.from_user.id
    print(chat_id)
    data = {
        'chat_id': chat_id,
    }
    if call.data == 'login':

        response = requests.post(telegram_urls.verify_url, data)

        if response.status_code == 200:

            response_text = response.json().get('response')
            username = str(response.json().get('username'))

            if response_text == 'registerd':
                bot.answer_callback_query(
                    call.id, 'You are already logged in.')
            else:
                bot.answer_callback_query(
                    call.id, 'You opted to login your account')
                bot.send_message(chat_id, 'You opted to login your account')
                bot.send_message(chat_id, 'Enter username:')
                bot.register_next_step_handler(call.message, handle_username)

        else:
            print('Verification failed', response)

    elif call.data == 'register':
        bot.send_message(chat_id, 'You opted to register as new member')
        bot.send_message(chat_id, 'Registration Begins')
        bot.send_message(chat_id, 'Enter username:')
        bot.register_next_step_handler(call.message, reg_username)

    elif call.data == 'logout':
        response = requests.post(telegram_urls.logout_url, data)
        resp = response.json().get('result')
        print('============1111111', resp)
        if resp == 'logout_success':
            bot.send_message(
                chat_id, 'You are sucessfully logged out from the system')
        else:
            bot.send_message(chat_id, 'You are not logged yet.')


temp_usr_details = []


@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text
    bot.reply_to(message, 'Great! Now enter your password.')

    bot.register_next_step_handler(message, handle_password, username)


def handle_password(message, username):
    password = message.text
    chat_id = message.chat.id
    user = {
        'chat_id': chat_id,
        'username': username,
        'password': password,
        'status': 0
    }

    temp_usr_details.append(user)

    response = requests.post(telegram_urls.login_url, user)
    print(response)
    response_out = response.json().get('status')
    username1 = response.json().get('username')
    print(response_out)
    if response_out == 'authenticated':
        bot.send_message(
            chat_id, f"Hi, {username1}! Welcome back.", reply_markup=telegram_markup.logout_markup)

    if response_out == 'not_authenticated':
        response_msg = response.json().get('message')
        bot.send_message(chat_id,f'{response_msg}')
        bot.reply_to(message, "Hi, I can't identify you please login or register",
                         reply_markup=telegram_markup.not_logined_markup)


def reg_username(message):
    username = message.text
    verif1 = telegram_func.validate_username(username)
    verif = json.loads(verif1)
    print('=+================',verif)
    if verif['status'] :
        bot.reply_to(message, 'Great! Now enter your email.')
        bot.register_next_step_handler(message, reg_email, username)
    else:
        result =verif['result']
        bot.reply_to(message, f'{result} , so please enter your username again.')
        bot.register_next_step_handler(message, reg_username)


def reg_email(message,username):
    email = message.text
    verif= telegram_func.validate_email(email)
    if verif :
        bot.reply_to(message, 'Great! Now enter your password.')
        bot.register_next_step_handler(message, reg_password, username,email)
    else:
        bot.reply_to(message, 'please enter your email again.')
        bot.register_next_step_handler(message, reg_email,username)

def reg_password(message,username,email):

    chat_id = message.chat.id
    password = message.text
    print (password)

    verif1= telegram_func.validate_password(password)
    verif = json.loads(verif1)
    if verif['status'] :
        data ={
            "username":username,
            "email":email,
            "password":password,

        }
        response = requests.post(telegram_urls.register_user,data)
        response_out = response.json().get('resp')
        if response_out == 'registred':
            bot.send_message(chat_id,'registred sucessfully')
        else:
            bot.send_message(chat_id,'sommething went wrong')   
    else:
        result = verif['result']
        bot.reply_to(message, f'{result} , so please enter your password again.')
        bot.register_next_step_handler(message, reg_password,username,email)







bot.polling()
