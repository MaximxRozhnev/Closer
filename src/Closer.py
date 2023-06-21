import psutil
import threading
import time
import ctypes

def Kill():
    processes = []
    with open('Process.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n\r')  # Удаление символов \n и \r
            processes.append(line)

    while True:
        time.sleep(3)
        countProccesses = dict() # Count of need processes
        for elem in psutil.process_iter():
            name = elem.name()

            countProccesses.setdefault(name, 0)
            countProccesses[name] += 1
            if countProccesses[name] > 1 and name in processes:
                elem.terminate()
                show_message_box("1С уже запущено на вашем компьютере!", "1C ошибка запуска", 0)


def show_message_box(text, header, times):
    ctypes.windll.user32.MessageBoxW(None, text, header, times)

# Вызов функции для вывода сообщения


Killer = threading.Thread(target = Kill)
Killer.start()