import telebot

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