import telebot
import requests

baseurl ='https://dept-experience-effects-stay.trycloudflare.com'

bot = telebot.TeleBot('5998807810:AAFUC9cd2s0vn_RAvl8YIKn6Z6fu8pj5i_A')

verify_url = baseurl +'/api/verify_user/'
login_url = baseurl +'/api/login/'
logout_url = baseurl +'/api/logout/'


not_logined_markup = telebot.types.InlineKeyboardMarkup()
logout_markup = telebot.types.InlineKeyboardMarkup()

    # Create inline keyboard buttons
button1 = telebot.types.InlineKeyboardButton(text='Login', callback_data='login')
button2 = telebot.types.InlineKeyboardButton(text='Register', callback_data='register')
login = telebot.types.InlineKeyboardButton(text='Login', callback_data='login')
logout = telebot.types.InlineKeyboardButton(text='logout', callback_data='logout')


    # Add the buttons to the markup
not_logined_markup.add(button1, button2)
logout_markup.add(logout)

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    text = message.text


    data = {
        'chat_id': chat_id,
        'text': text
    }
    print(chat_id)
    response = requests.post(verify_url, data)

    if response.status_code == 200:

        
        response_text = response.json().get('response')
        username = str(response.json().get('username'))

        if response_text == 'registerd':
            bot.send_message(chat_id, f"Hii "+ username,reply_markup=logout_markup )
        else:
           bot.reply_to(message, "Hi, I can't identify you please login or register",reply_markup=not_logined_markup) 

        
    else:
        print('Verification failed',response)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text


    data = {
        'chat_id': chat_id,
        'text': text
    }
    print(chat_id)
    response = requests.post(verify_url, data)

    if response.status_code == 200:

        
        response_text = response.json().get('response')
        username = str(response.json().get('username'))

        if response_text == 'registerd':
            bot.send_message(chat_id, f"Hii "+ username,reply_markup=logout_markup )
        else:
           bot.reply_to(message, "Hi, I can't identify you please login or register",reply_markup=not_logined_markup) 

        
    else:
        print('Verification failed',response)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id =call.from_user.id
    print(chat_id)
    data = {
        'chat_id': chat_id,
     }
    if call.data == 'login':

        response = requests.post(verify_url, data)

        if response.status_code == 200:

        
            response_text = response.json().get('response')
            username = str(response.json().get('username'))

            if response_text == 'registerd':
                bot.answer_callback_query(call.id, 'You are already logged in.')
            else:
                bot.answer_callback_query(call.id, 'You opted to login your account')
                bot.send_message(chat_id, 'Enter your username:')
                bot.register_next_step_handler(call.message, handle_username) 

        
        else:
            print('Verification failed',response)

        
    elif call.data == 'register':
        bot.answer_callback_query(chat_id, 'You opted to register as new member')

    elif call.data == 'logout':
        response = requests.post(logout_url, data)
        resp =response.json().get('result')
        print('============1111111',response)
        if resp == 'logout_sucess':
            bot.send_message(chat_id, 'You are sucessfully logged out from the system')
        else:
            bot.send_message(chat_id, 'You are not logged yet.')   


        

temp_usr_details = []
@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text
    bot.reply_to(message, 'Great! Now enter your password.')

    bot.register_next_step_handler(message, handle_password,username)

def handle_password(message,username):
    password = message.text
    chat_id = message.chat.id
    user = {
        'chat_id' : chat_id,
        'username': username,
        'password': password,
        'status': 0
    }

    temp_usr_details.append(user)

    response = requests.post(login_url, user)
    response_out = response.json().get('status')

    if response_out == 'authenticated' :
        bot.send_message(chat_id, f"Hi, {message.chat.first_name}! Welcome back.",reply_markup=logout_markup)

    if response_out == 'not_authenticated' :
        bot.register_next_step_handler(message, callback_handler,user)   






bot.polling()