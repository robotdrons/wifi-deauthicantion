from os import system
print("Введите сетевой адаптер\n\n")
system("sudo airmon-ng")
adapter = input()
system("sudo airmon-ng start " + adapter)
system("xterm -e 'python3 6.py' & xterm -e 'python3 7.py'")
print("Спасибо за пользования")
system("airmon-ng stop wlan0mon")

      
