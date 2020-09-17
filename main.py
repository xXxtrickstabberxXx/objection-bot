import requests
import json
from longpoll import LongPollApi

access_token=""
group_id=""
my_token=""
bot=LongPollApi(access_token,group_id,my_token)
while 1:
    bot.events()
