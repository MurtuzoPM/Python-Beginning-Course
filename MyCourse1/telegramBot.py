# import requests

# # Параметры Telegram API
# TOKEN = '7042171541:AAGl9NE7zNjmrpqeVvWhsowone3WcNiyT1M'
# CHAT_ID = '-4512801834'

# def send_message_to_telegram(message):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#     payload = {
#         'chat_id': CHAT_ID,
#         'text': message
#     }
#     response = requests.post(url, data=payload)
#     return response

# def filter_and_send_logs(file_path, ip_address):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     for line in lines:
#         if ip_address in line:
#             response = send_message_to_telegram(line)
#             if response.status_code != 200:
#                 print(f"Ошибка отправки сообщения: {response.text}")

# if __name__ == "__main__":
#     log_file_path = 'C:\\Users\\murtuzo.mamadziyoev\\OneDrive - University of Central Asia\\Desktop\\python tutors\\New Course1\\log.txt'
#     target_ip = '192.168.5.10'
#     filter_and_send_logs(log_file_path, target_ip)

import requests

def read_log_file(file_path, ip_address):
    """
    Чтение файла и возврат всех строк, содержащих указанный IP-адрес.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    matching_lines = [line for line in lines if ip_address in line]
    return matching_lines

def send_message_to_telegram(token, chat_id, message):
    """
    Отправка сообщения в Telegram.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.status_code == 200

def main(log_file_path, ip_address, telegram_token, chat_id):
    # Поиск строк, содержащих IP-адрес
    matching_lines = read_log_file(log_file_path, ip_address)

    # Если найдено соответствие, отправка сообщений в Telegram
    if matching_lines:
        for line in matching_lines:
            send_message_to_telegram(telegram_token, chat_id, line)
    else:
        print("Совпадения не найдены.")

if __name__ == "__main__":
    log_file_path = 'C:\\Users\\murtuzo.mamadziyoev\\OneDrive - University of Central Asia\\Desktop\\python tutors\\New Course1\\log.txt'  # Путь к файлу с логами
    ip_address = '192.168.5.10'  # Введите здесь IP-адрес для поиска
    telegram_token = '7042171541:AAGl9NE7zNjmrpqeVvWhsowone3WcNiyT1M'  # Введите здесь ваш токен бота Telegram
    chat_id = '-4512801834'  # Введите здесь ID вашей Telegram-группы

    main(log_file_path, ip_address, telegram_token, chat_id)

