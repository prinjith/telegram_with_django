# Telegram with DJANGO
This project aims to integrate Telegram with a Django web application through an API to provide registration and login functionality. The goal is to allow users to register and log in to the Django web application using their Telegram accounts


In this project, a Django app and Telegram are connected through an intermediate custom Python module called "telegram_bot." Each of the three systems works independently and is connected using APIs.

Within the Django app, endpoints for login, authentication, and registration are created. The custom Telegram module communicates with these endpoints, calling them based on the responses received from Telegram. It generates responses according to the responses from the Django endpoints.

By using this module, any Django system can be connected to Telegram. Users can access their data in the Django system. For example, in an e-commerce site, users can track their orders and check the availability of products etc. This can be achieved by creating endpoints in Django and adding code to the "telegram_bot" module. All functions are implemented through APIs, making it easy to connect to any system.


we can give QR code for the telegram in django, and we can join to the bot through that
![Screenshot from 2023-06-01 18-25-38](https://github.com/prinjith/telegram_with_django/assets/115553509/baf758d8-13b2-41f3-afa3-de0620952bcf)

