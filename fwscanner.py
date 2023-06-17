# -*- coding: utf-8 -*-
import requests
print("""
  _           _         _    _           _   _               ________          __   _____                                 
 | |         | |       | |  | |         | | (_)             |  ____\ \        / /  / ____|                                
 | |    _   _| | ____ _| |__| | ___  ___| |_ _ _ __   __ _  | |__   \ \  /\  / /  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | |   | | | | |/ / _` |  __  |/ _ \/ __| __| | '_ \ / _` | |  __|   \ \/  \/ /    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |___| |_| |   < (_| | |  | | (_) \__ \ |_| | | | | (_| | | |       \  /\  /     ____) | (_| (_| | | | | | | |  __/ |   
 |______\__,_|_|\_\__,_|_|  |_|\___/|___/\__|_|_| |_|\__, | |_|        \/  \/     |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                      __/ |                                                               
                                                     |___/                                                                

 """)
def detect_waf(url):
    headers = {
        'User-Agent': 'me bakıyorsun olm user-agent bu'
    }

    wafs = [
        'mod_security', 'owasp', 'bigip', 'netscaler', 'fortinet', 'sonicwall',
        'palo alto', 'imperva', 'barracuda', 'juniper', 'cloudflare', 'incapsula',
        'akamai', 'f5', 'citrix', 'radware', 'fastly'
    ]

    for waf in wafs:
        headers['User-Agent'] = waf
        response = requests.get(url, headers=headers)
        if response.status_code == 403:
            print(f"{waf} Web Uygulama Güvenlik Duvarı algılandı.")
        else:
            print(f"{waf} Web Uygulama Güvenlik Duvarı algılanamadı.")


url = input("URL : ")

detect_waf(url)
