import telegram_settings


baseurl = telegram_settings.HOST_URL


verify_url = baseurl +'/api/verify_user/'
login_url = baseurl +'/api/login/'
logout_url = baseurl +'/api/logout/'
register_user = baseurl +'/api/register/'