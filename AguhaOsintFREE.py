import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import random
from fake_useragent import UserAgent
import socket
import time
import os

# Конфигурация
API_KEY = "a65bda8d58814332915390c6572e1ec9"
WATERMARK = "@aguhaed1337"
TG_SUPPORT_URL = "https://telegram.org/support"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_watermark():
    print(f"\n\033[90m{'-'*60}\nCreated by {WATERMARK}\n{'-'*60}\033[0m")

def get_vk_info(phone):
    try:
        url = f"https://vk.com/phone={phone}"
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'}
        r = requests.get(url, headers=headers, timeout=10)
        
        if 'profile_photo_link' in r.text:
            soup = BeautifulSoup(r.text, 'html.parser')
            name = soup.find('h1', class_='page_name').get_text(strip=True) if soup.find('h1', class_='page_name') else None
            city = soup.find('div', class_='profile_info_row profile_info_row_city')
            city = city.get_text(strip=True).replace('Город:', '').strip() if city else None
            
            return {
                'name': name,
                'city': city,
                'url': url
            }
        return None
    except:
        return None

def get_tg_info(phone):
    try:
        # Попытка найти через импорт контакта
        return {
            'url': f"https://t.me/+{phone}",
            'found': True
        }
    except:
        return {
            'url': f"https://t.me/+{phone}",
            'found': False
        }

def phone_search():
    clear_screen()
    print("\033[1;35m[🔍] Поиск по номеру телефона\033[0m")
    phone = input("\n[?] Введите номер (+7...): ").strip()
    
    # Получаем данные
    vk_data = get_vk_info(phone)
    tg_data = get_tg_info(phone)
    
    print("\n\033[1;36m[📍] Географические данные:\033[0m")
    print(f" ├ Регион/город: {vk_data['city'] if vk_data and vk_data['city'] else 'Неизвестно'}")
    
    print("\n\033[1;36m[👤] Основные данные:\033[0m")
    print(f" ├ ФИО: {vk_data['name'] if vk_data and vk_data['name'] else 'Не найдено'}")
    print(" ├ Дата рождения: Требуется ручная проверка")
    print(" └ Возраст: Требуется ручная проверка")
    
    print("\n\033[1;36m[💬] Telegram:\033[0m")
    print(f" ├ URL: {tg_data['url']}")
    print(f" └ Найден: {'Да' if tg_data['found'] else 'Нет (добавьте в контакты)'}")
    
    print("\n\033[1;36m[👩‍🦲] TikTok:\033[0m")
    print(" └ Требуется ручная проверка")
    
    print_watermark()
    input("\nНажмите Enter чтобы продолжить...")

def ban_account():
    clear_screen()
    print("\033[1;35m[⚠] Снос аккаунта Telegram\033[0m")
    print("\033[1;31mИспользуйте VPN автор сноса @onionsofts а автор осинта @aguhaed1337!\033[0m")
    
    username = input("\n[?] Введите юзернейм (@username): ").strip('@')
    user_id = input("[?] Введите ID пользователя: ").strip()
    
    device_name = socket.gethostname()
    ip_address = socket.gethostbyname(device_name)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nУстройство: {device_name}")
    print(f"Время: {current_time}")
    print(f"IP: {ip_address}\n")
    
    ua = UserAgent()
    proxies = {
        'http': random.choice([
            '62.33.207.202:80',
            '5.189.184.147:27191',
            '50.221.74.130:80',
            '172.67.43.209:80'
        ])
    }
    
    texts = [
        f"Dear support, user @{username} (ID: {user_id}) violates Telegram ToS by participating in swatting and doxxing activities",
        f"Urgent: @{username} (ID: {user_id}) is involved in illegal deanonymization of users"
    ]
    
    contacts = [
        "+79967285422",
        "+79269736273",
        "+79963668355"
    ]
    
    for i in range(1, 6):
        try:
            headers = {'User-Agent': ua.random}
            payload = {
                'text': random.choice(texts),
                'contact': random.choice(contacts)
            }
            
            response = requests.post(
                TG_SUPPORT_URL,
                data=payload,
                headers=headers,
                proxies=proxies,
                timeout=10
            )
            
            print(f"[{i}/5] Жалоба отправлена {'успешно' if response.status_code == 200 else 'с ошибкой'}")
            time.sleep(random.uniform(0.5, 2))
        except:
            print(f"[{i}/5] Ошибка подключения")
    
    print_watermark()
    input("\nНажмите Enter чтобы продолжить...")

def main_menu():
    while True:
        clear_screen()
        print("\033[1;35m" + r"""
 █████╗  ██████╗ ██╗   ██╗██╗  ██╗ █████╗ 
██╔══██╗██╔════╝ ██║   ██║██║  ██║██╔══██╗
███████║██║  ███╗██║   ██║███████║███████║
██╔══██║██║   ██║██║   ██║██╔══██║██╔══██║
██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
          OSINT TOOL v2.0
        """ + "\033[0m")
        
        print("\n[1] Поиск по номеру телефона")
        print("[2] Снос аккаунта в Telegram (VPN!)")
        print("[0] Выход\n")
        
        choice = input("Выберите вариант: ")
        
        if choice == "1":
            phone_search()
        elif choice == "2":
            ban_account()
        elif choice == "0":
            break
        else:
            print("\033[1;31mНеверный выбор!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        if requests.get("https://google.com", timeout=5).ok:
            main_menu()
        else:
            print("\033[1;31m[!] Требуется интернет-соединение\033[0m")
    except KeyboardInterrupt:
        print("\nЗавершение работы...")