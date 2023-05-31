import requests
import telegram_urls


username = 'user12234'
password = 'user'
email= 'user12234@gmail.com'

data ={
    'username':username,
    'password':password,
    'email':email
}

response = requests.post(telegram_urls.register_user, data)


# result = str(response.json().get('resp'))
# print(response)
print('================',response)
# print(response.result)