
import webbrowser
import pyautogui
import time

time.sleep(3)
# abrindo os perfis digitais
# Abre o github
webbrowser.open("https://github.com/oGomesThiago")
time.sleep(3)
# Abre o linkedin
webbrowser.open("https://www.linkedin.com/in/thiago-gomes-490922184/")
time.sleep(5)

# Abre a plataforma da twitch
webbrowser.open("https://www.twitch.tv/biiribiinha")
time.sleep(4)

# Abrir VS Code caso tenha
pyautogui.hotkey("winleft")
pyautogui.write("Visual")
time.sleep(1)
pyautogui.press("enter")

print("Obrigado!")