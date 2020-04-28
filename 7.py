from os import system
print("Нажмите Ctrl+C что бы остановить сканирования и скопировать Мас адреса\n Подождите 3 секунды")
system("sleep 3")
system("sudo airodump-ng wlan0mon")
print("Нажмите ENTER чтобы продолжить")
input()
system("sudo airodump-ng wlan0mon")
