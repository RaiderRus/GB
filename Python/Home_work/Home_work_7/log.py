# модуль для записи лога

import datetime

def log_data(s):
    dt = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    s = 'Дата и время:' + ' ' + dt + '; ' + s + '\n'
    with open('log_file.txt', 'a', encoding='utf-8') as l:
        l.write(s)
