from discord import Webhook, RequestsWebhookAdapter
import os
import time
URL = "null"
os.system('clear')
if URL == 'null':
    print('WARNING!!! NO WEBHOOK SET!!!')
    URL = input('Your webhook: ')
    webhook = Webhook.from_url(URL, adapter = RequestsWebhookAdapter())
    print('Webhook is now set!')
time.sleep(1)
os.system('clear')
print('===Webhook messager===')
print('type !help for commands')
print('======================')
while True:
    messagew = input('Your message: ')
    if messagew == '!help':
        print('''===Help command===
!exit - exits the messager
!change - change your webhook
!spam - spam 
=================''')
    elif messagew == '!exit':
        break
    elif messagew == '!change':
        URL = input("Your new webhook: ")
        webhook = Webhook.from_url(URL, adapter = RequestsWebhookAdapter())
        print('Webhook is now set!')
    elif messagew == '!spam':
        messagew = input('Your message to spam: ')
        spamcount = input("How many times: ")
        spamcount = int(spamcount)
        for _ in range(spamcount):
            webhook.send(messagew)    
    else:    
        webhook.send(messagew)
